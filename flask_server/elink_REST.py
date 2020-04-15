import flask
import requests
import jsonify

app = flask.Flask(__name__)


@app.route("/execution_REST_API", methods=["POST"])						##dummy REST API 
def execution_links_accept():
	
	ack = {"success": False}
	
	if flask.request.method == "POST":
		#print request.data
		if flask.request.is_json:
			content = flask.request.get_json()
			print ("execution_REST_API_dummy")	
			print content
			
			ack["success"] = True

	return flask.jsonify(ack)


if __name__ == "__main__":
	print(" Flask starting server...")
	app.run(port=5001, debug=True)
