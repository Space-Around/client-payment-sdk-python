from client_payment_sdk import Webhook, WebhookData, SignatureVerificationError
from flask import Flask, request
import os


app = Flask(__name__)
api_secret = 'aa21444f3f71'


@app.route("/webhooks", methods=["POST", "GET"])
def webhooks():
    payload = request.form.to_dict()
    try:
        data = WebhookData(payload)

        print(Webhook.verify_signature('/webhooks', 'POST', data, api_secret))
        # usage data
    except ValueError:
        print("Error while decoding event!")
        return "Bad payload", 400
    except SignatureVerificationError:
        print("Invalid signature!")
        return "Bad signature", 400

    return "", 200


if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 5000)))
