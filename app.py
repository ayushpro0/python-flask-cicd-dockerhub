from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello, Dockerized Python!"})

@app.route("/echo", methods=["POST"])
def echo():
    data = request.json
    return jsonify({"you_sent": data}), 200

if __name__ == "__main__":
    # Run with host=0.0.0.0 so container can expose it
    app.run(host="0.0.0.0", port=5000)
