
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Salam ! Bienvenue sur MCEA IA Mentor 🚀"

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get("Body", "").lower()

    response = MessagingResponse()
    message = response.message()

    if "bonjour" in incoming_msg:
        message.body("Salam 👋 Bienvenue sur MCEA IA Mentor 🚀")
    else:
        message.body("Je suis MCEA IA Mentor. Comment puis-je vous aider ?")

    return str(response)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080))
    )

























if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
