"""
Outgoing buy/sell/modify JSON :
[
	{
	"type" : "value",
	"transactionID" : "value",
	"symbol" : "value",
	"size" : "value",
	"client" : "value",
	"exchange" : "value",
	"counterParty"  : "value",
	"symbolDescription"  : "value",
	"priceInstruction"  : "value",
	"clientDescription"  : "value",
	"account"  : "value",
	"limit"  : "value",
	"TIF"  : "value"
	}
]

Incoming buy/sell/modify JSON : 
[
    {
    "errno" : "value",
    "error" : "value",
    }
]


Outgoing staus JSON :
[
    {
    "transactionID" : "value",
    "Exchange" : "value",
    }
]


Incoming update JSON : 
[
    {
    "orderID"  : "value",
    "side" : "value",
    "state" : "value",
    "client" : "value",
    "size" : "value",
    "qtyDone" : "value",
    "priceInstr" : "value",
    "price"  : "value",
    "exchange"  : "value",
    "prodType"  : "value",
    "ask"  : "value",
    "bid"  : "value",
    "LTP"  : "value",
    "cntrParty"  : "value",
    "orderStamp"  : "value",
    "username"  : "value"
    }
]


"""
