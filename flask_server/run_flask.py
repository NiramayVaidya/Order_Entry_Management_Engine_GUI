
import requests
import jsonify

from flask import Flask

app = Flask(__name__)

def send_to_exec_link(new_order, new_order_id, content_type):							## send to execution link
	# initialize the REST API endpoint URL
	URL_FOR_ORDER = "http://localhost:5001/execution_REST_API"
	
	headers = {'Content-Type' : 'application/json'}

	order_data = {'type': content_type, 'transactionID': str(new_order_id), 
			'symbol' : new_order['symbol'], 'size': new_order['size'], 
			'client' : new_order['client'], 'counterParty': new_order['counterParty'], 
			'symbolDescription': new_order['symbolDescription'], 'clientDescription' : new_order['clientDescription'], 
			'account' : new_order['account'], 'exchange' : new_order['exchange'], 
			'priceInstruction' : new_order['priceInstruction'] ,'limit':neworder['limit'], 'TIF' : new_order['TIF']}
			

	if content_type == 1:
		URL = " http://localhost:5050/orders/buy"
		
	elif content_type == 2:
		URL = " http://localhost:5050/orders/sell"
		
	elif content_type == 3:
		URL = " http://localhost:5050/orders/modify"
	
	else:
		URL = " http://localhost:5050/orders/status"
		
	
	# submit the request
	#exec_ack = requests.post(URL_FOR_ORDER, data = json.dumps(order_data), headers = headers).json()
	return exec_ack


def send_to_trade_post(order):				
	# initialize the REST API endpoint URL
	URL_FOR_ORDER_FILL = "http://localhost:5002/trade_post_REST_API"
	headers = {'Content-Type' : 'application/json'}

	order_fill_data = {'orderID': str(order['_id']), 'state': order['state'], 
				'client' : order['client'], 'side': order['side'], 'prodType':order['prodType'],
				'ask': order['ask'], 'qtyDone' : order['qtyDone'], 'cntrParty': order['cntrParty'], 
				'orderStamp' : order['orderStamp'], 'priceInstr' : order['priceInstr'],
				'price' : order['price'], 'LTP' : order['LTP'] , 'bid' : order['bid'], 'prodType': order['prodType'], 'username': order['username']}

	# submit the request
	r = requests.post(URL_FOR_ORDER_FILL, data = json.dumps(order_fill_data), headers = headers).json()

	# ensure the request was sucessful
	if r["success"]:
		print ('Request succeeded')
		
	# otherwise, the request failed
	else:
		print ("Request failed")

if __name__ == "__main__":
	print(" Flask starting server...")
	app.run(debug=True)
