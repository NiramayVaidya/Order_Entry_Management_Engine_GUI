import json
import datetime
from Code_Parse import parse_message
from Code_Templates_Groups import Heartbeat
from Code_Templates_Groups import NewOrderSingle
from Code_Templates_Groups import OrderCancelRequest
from Code_Templates_Groups import OrderCancelReplaceRequest
from Code_Templates_Groups import Logon
from Code_Templates_Groups import Logout
from Code_Templates_Groups import Instrument
from Code_Templates_Groups import OrderQtyData

import threading

import mysql.connector


msgseqnum = 0

# the server address will be fixed
targetcompid = 1

# fix the heartbeat interval in seconds
heartbeatint = 100

# assuming the encryption method to be none
encryptmethod = 0

timer = threading.Timer(heartbeatint, Heartbeat, msgseqnum, targetcompid)

	 
mydb = mysql.connector.connect(host='localhost',user='root',passwd='INDERneel@1998',db='EXCHANGE_INFO')
mycursor = mydb.cursor()


def logonmain() :
	global msgseqnum
	global timer
	# Log on message will be the first in the sequence
	msgseqnum = 1
	if not timer.is_alive():
		timer.start()
	return Logon(msgseqnum, targetcompid, encryptmethod, heartbeatint)

# Call this everytime a json object is received

# for cancel order and modify order we need to retrieve order info from db referring the original ID and then create a new ID for the modified one. Then call ordercancelreplacerequest/ordercancelrequest with that data. Just do this @Neil

logonmain()

def mainreceive(json_string) :
	
	global msgseqnum
	global timer

	msgseqnum = msgseqnum + 1
	tempdatadict = json.loads(json_string)

	ordertype = tempdatadict.get("type")
	symbol = tempdatadict.get("Symbol")
	size = int(tempdatadict.get("size"))
	i = Instrument(Symbol = symbol)
	ordersize = OrderQtyData(OrderQty = size)
	clordid = tempdatadict.get("transactionID")
	account = tempdatadict.get("account")
	tempprice = tempdatadict.get("PriceInstruction")
	tifid = tempdatadict.get("TIF")
	ordtype = -1
	tif = -1
	side = -1
	
	if ordertype == "Buy" :
		side = '1'
	elif ordertype == "Sell":
		side = '2'
	elif (ordertype == "Modify" or ordertype == "Cancel") :
		side = side

	transacttime = datetime.datetime.now()
        
	if tempprice == "Limit" :
		ordtype = "2"
	elif tempprice == "Limit Close" :
		ordtype = "B"
	elif tempprice == "Limit Open" :
		ordtype = "2"
	elif tempprice == "Market" :
		ordtype = "1"
	elif  tempprice == "Market Open" :
		ordtype = "1"
	elif tempprice == "Market Close" :
		ordtype = "5"

	if tifid == "Day Order" :
		tif = "0"
	elif tifid == "Fill or kill order" :
		tif = "4"
	elif tifid == "Good till cancelled" :
		tif = "1"
	elif tifid == "Good till date" :
		tif = "6"
	elif tifid == "Immediate or cancel order" :
		tif = "3"
        
	timer.cancel()
	
	if not timer.is_alive():
		timer.start()	
		
	#NewOrderSingle Message
	if ordertype == "Buy" or ordertype == "Sell":
		sql = "INSERT INTO Exchg_Info (msgseqnum, clOrdID, side, ordtype, i, ordersize, Account, TimeInForce) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
		val = (msgseqnum, clordid, side, ordertype, i.tag_vals[0][1], ordersize.tag_vals[0][1], account, tifid)
		mycursor.execute(sql, val)
		mydb.commit()
		return NewOrderSingle(MsgSeqNum = msgseqnum, TargetCompID = targetcompid, ClOrdID = clordid, Side = side, TransactTime = transacttime, OrdType = ordtype, Instrument = i, OrderQtyData = ordersize, Account = account, TimeInForce = tif)
	
	#OrderCancelReplaceRequest
	elif ordertype == "Modify":
		#ClordID = 
		sql1 = "UPDATE Exchg_Info SET msgseqnum = %s, clOrdID = %s, side = %s, ordtype = %s, i = %s, ordersize = %s, Account = %s, TimeInForce = %s WHERE clOrdID = %s"
		val1 = (msgseqnum, clordid, side, ordertype, i.tag_vals[0][1], ordersize.tag_vals[0][1], account, tifid, ClordID)
		mycursor.execute(sql1, val1)
		mydb.commit()
		return OrderCancelReplaceRequest(MsgSeqNum = msgseqnum, TargetCompID = targetcompid, OrigClOrdID = ClordID, ClOrdID = clordid, Side = side, TransactTime = transacttime, OrdType = ordtype, Instrument = i, OrderQtyData = ordersize, Account = account, TimeInForce = tif)
	
	#OrderCancelRequest()
	elif ordertype == "Cancel":
		ClordID = tempdatadict.get("transactionID")
		sql2 = "DELETE FROM Exchg_Info WHERE clOrdID = %s"
		val2 = (clordid,)
		mycursor.execute(sql2, val2)
		mydb.commit()
		return OrderCancelRequest(MsgSeqNum = msgseqnum, TargetCompID = targetcompid, OrigClOrdID = clordid, ClOrdID = ClordID, Side = side, TransactTime = transacttime, Instrument = i, OrderQtyData = ordersize, Account = account)

def mainsend(msg) :
	
	global timer
	timer.cancel()
	if not timer.is_alive():
		timer.start()

	return parse_message(msg)

def logoutmain() :
	
	global timer
	global msgseqnum
	timer.cancel()
		
	msgseqnum = msgseqnum + 1
	return Logout(msgseqnum, targetcompid)

my_json_string = json.dumps({'type': "Modify", 'Symbol': "DEC", 'size': "30", "transactionID" : "4FH", 'account': "GHF5", 'PriceInstruction': "thr6", 'TIF': "fhrhy"})

mainreceive(my_json_string)
