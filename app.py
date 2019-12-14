from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

import json

def numero_destinataire(num_expediteur):

	num_expediteur = num_expediteur[4:]

	with open('correspondance.json') as myfile:
		obj = json.loads(myfile.read())

	return  obj[0][num_expediteur]

account_sid = 'ACc3e070169a034ce2c67a0dde60f7e093' 
auth_token = '969faef6f728a75fa0bdbd7b84c50378' 
client = Client(account_sid, auth_token) 


app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
	"""Respond to incoming calls with a simple text message."""
	# Fetch the message

	msg = request.form.get('Body')
	from_ = request.form.get('From')
	to = numero_destinataire(from_)

	# Create reply
	resp = MessagingResponse()

	message = client.messages.create( 
		from_='whatsapp:+14155238886',  
		body='Your appointment is coming up on July 21 at 3PM',      
		to='whatsapp:+228'+to
	)
	print("####", message.sid)

	resp.message("")

	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)