from flask import Flask, request, jsonify
from twilio.twiml.voice_response import VoiceResponse, Dial
# Add CORS support
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from twilio.rest import Client
SID = None
ACCOUNT_SID = ''
AUTH_TOKEN = ''
client = Client(ACCOUNT_SID, AUTH_TOKEN)

AGENT_PHONE_NUMBER = '+' 
TWILIO_PHONE_NUMBER = '+'
CUSTOMER_PHONE_NUMBER = '+'

CONVERSATION = [
    ("This call is from XXXX. We have an important message for you. A representative will be with you shortly.", 1)
    ]

ENDING_CALL = False

@app.route('/send-sms', methods=['POST'])
def send_sms():
    try:
        # Get JSON data from request
        data = request.json
        phone_number = data['phoneNumber']
        message = data['smsMessage']
    except KeyError as e:
        return jsonify(status='failed', error=f'Missing parameter: {e}')

    # Create a Twilio client
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    # Send the SMS
    message = client.messages.create(
        to=phone_number,
        from_=TWILIO_PHONE_NUMBER,
        body=message
    )

    return jsonify(status='success', sid=message.sid)

@app.route('/handle-incoming-call', methods=['POST'])
def handle_incoming_call():
    # The number to which the call will be forwarded
    forward_to_number = AGENT_PHONE_NUMBER
    
    response = VoiceResponse()
    response.say("Thank you for calling XXXX. Please wait while we connect you to a representative.")
    dial = Dial()
    dial.number(forward_to_number)
    response.append(dial)
    
    return str(response)

@app.route('/', methods=['GET'])
def index():
    # Show the page.html file in the root folder
    return app.send_static_file('page.html')

@app.route('/fallback', methods=['POST'])
def fallback():
    response = VoiceResponse()
    response.say("Thank you, a sales representative will call you shortly.")
    return str(response)

@app.route('/call', methods=['POST'])
def call():
    try:
        # Get JSON data from request
        data = request.json
    except Exception as e:
        return {
            'status': 'failed',
            'response': str(e)
        }
    # Get phone number from JSON
    phone_number = data['phoneNumber']
    call = client.calls.create(
        url='http://127.0.0.1/start',
        to=phone_number,
        from_=TWILIO_PHONE_NUMBER
    )
    global SID
    SID = call.sid
    return {
        'status': 'success',
        'response': str(call)
        }
@app.route('/start', methods=['POST'])
def start():
    response = VoiceResponse()
    response.say(CONVERSATION[0][0])
    response.dial(AGENT_PHONE_NUMBER)
    
    return str(response)

@app.route('/hold', methods=['POST'])
def hold():
    global SID
    call = client.calls(SID).update(
        method='POST',
        url='http://127.0.0.1/enqueue'
    )
    return {
        'status': 'success',
        'response': str(call)
    }

@app.route('/unhold', methods=['POST'])
def unhold():
    global SID
    call = client.calls(SID).update(
        method='POST',
        url='http://127.0.0.1/dequeue'
    )
    return {
        'status': 'success',
        'response': str(call)
    }

@app.route('/enqueue', methods=['POST'])
def enqueue_call():
    response = VoiceResponse()
    with response.enqueue(waitUrl="/hold-music") as enqueue:
        enqueue.task("customer_hold_queue")
    return str(response)
    
@app.route('/hold-music', methods=['POST'])
def hold_music():
    response = VoiceResponse()
    response.play('https://demo.twilio.com/docs/classic.mp3', loop=0)
    return str(response)

@app.route('/dequeue', methods=['POST'])
def dequeue_call():
    response = VoiceResponse()
    dial = Dial()
    dial.queue('customer_hold_queue')
    response.append(dial)
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)