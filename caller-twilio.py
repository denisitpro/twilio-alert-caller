from flask import Flask, jsonify, request
from twilio.rest import Client
import os
import sys

app = Flask(__name__)

# Load environment variables
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
twilio_number = os.environ.get('TWILIO_PHONE_NUMBER')
twiml_url = os.environ.get('TWIML_URL', 'http://demo.twilio.com/docs/voice.xml')  # Default to demo TwiML URL
host = os.environ.get('TWILIO_BIND_ADDRESS', '0.0.0.0')  # Default address is 0.0.0.0
port = int(os.environ.get('TWILIO_PORT', 5000))  # Default port is 5000

# Check for required environment variables
missing_env_vars = []
if not account_sid:
    missing_env_vars.append('TWILIO_ACCOUNT_SID')
if not auth_token:
    missing_env_vars.append('TWILIO_AUTH_TOKEN')
if not twilio_number:
    missing_env_vars.append('TWILIO_PHONE_NUMBER')

if missing_env_vars:
    print(f"Error: Missing required environment variables: {', '.join(missing_env_vars)}")
    sys.exit(1)  # Exit if required env vars are missing

# Initialize Twilio client
client = Client(account_sid, auth_token)

@app.route('/call/<to_number>', methods=['GET', 'HEAD', 'POST'])
def make_call(to_number):
    # If it's a HEAD request, just return an empty response
    if request.method == 'HEAD':
        return '', 200

    # For GET and POST methods, handle the call creation
    if not to_number:
        return jsonify({'error': 'Missing "to" phone number in URL.'}), 400

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