from flask import Flask, request, jsonify
from twilio.rest import Client
import os

app = Flask(__name__)

# Load environment variables
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
twilio_number = os.environ.get('TWILIO_PHONE_NUMBER')
twiml_url = os.environ.get('TWIML_URL', 'http://demo.twilio.com/docs/voice.xml')  # Default to demo TwiML URL

# Address binding variables
host = os.environ.get('TWILIO_BIND_ADDRESS', '0.0.0.0')  # Default address is 0.0.0.0
port = int(os.environ.get('TWILIO_PORT', 5000))  # Default port is 5000

# Initialize Twilio client
client = Client(account_sid, auth_token)

@app.route('/call', methods=['POST'])
def make_call():
    # Get the 'to' phone number from the request
    data = request.json
    to_number = data.get('to')

    if not to_number:
        # Return an error if the 'to' number is missing
        return jsonify({'error': 'Missing "to" phone number in request.'}), 400

    try:
        # Initiate the call using the Twilio API
        call = client.calls.create(
            to=to_number,
            from_=twilio_number,
            url=twiml_url  # Use the TwiML URL for handling the call
        )
        # Return a success response with the call SID
        return jsonify({'message': 'Call initiated', 'call_sid': call.sid})
    except Exception as e:
        # Return an error response in case of failure
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Start the Flask app on the specified address and port
    app.run(host=host, port=port)