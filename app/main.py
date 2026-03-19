from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "Hello from CI Demo!", "status": "running"})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/api/greet/<name>")
def greet(name):
    return jsonify({"greeting": f"Hello, {name}!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
