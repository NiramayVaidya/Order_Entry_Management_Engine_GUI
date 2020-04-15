import flask
import requests
import jsonify

app = flask.Flask(__name__)


@app.route("/trade_post_REST_API", methods=["POST"])						##dummy REST API 
def trade_post_accept():
	
	ack = {"success": False}
	
	if flask.request.method == "POST":
		#print request.data
		if flask.request.is_json:
			content = flask.request.get_json()
			print ("trade_post_REST_API_dummy")	
			print content
			
			ack["success"] = True

	return flask.jsonify(ack)



if __name__ == "__main__":
	print(" Flask starting server...")
	app.run(port=5002, debug=True)