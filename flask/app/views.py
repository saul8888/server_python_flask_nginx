from app import app

@app.route("/")
def hello():
	return "<h1 style='color:blue'>HELLO WORD!</H1>"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80,debug=True)