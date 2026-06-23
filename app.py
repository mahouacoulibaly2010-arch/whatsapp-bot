from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Bonjour Mahoua"

@app.route("/webhook", methods=["POST"])
def webhook():
    print(request.form)
    return "OK"

if __name__ == "__main__":
    app.run(port=5000)
