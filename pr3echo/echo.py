
from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=["POST"])
def echo():
    data = request.data.decode("utf-8")  # get raw body
    print("Received:", data)
    return f"Echoed: {data}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
