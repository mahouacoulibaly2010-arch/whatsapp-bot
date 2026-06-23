from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Bonjour Mahoua"

@app.route("/webhook", methods=["POST"])
def webhook():
    print(request.form)
    return "OK"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
