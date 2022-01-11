from client_payment_sdk import Webhook, SignatureVerificationError
from flask import Flask, request
import os


app = Flask(__name__)
api_secret = 'aa21444f3f71'


@app.route("/webhooks", methods=["POST"])
def webhooks():
    payload = request.data.decode("utf-8")

    try:
        # wh = Webhook(payload, api_secret)
        # wh.verify_signature()
        # notification = wh.to_class()

        notification = Webhook.verify_signature(payload, api_secret)

        # usage notification
    except ValueError:
        print("Error while decoding event!")
        return "Bad payload", 400
    except SignatureVerificationError:
        print("Invalid signature!")
        return "Bad signature", 400

    return "", 200


if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 5000)))
