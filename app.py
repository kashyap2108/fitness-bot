import os,sys
from flask import Flask,request
from utils import wit_response
import json
import requests
from pymessenger import Bot
from fbmq import Page,Attachment,Template,QuickReply

app = Flask(__name__)


PAGE_ACCESS_TOKEN = 'EAAbYwLFXiZAABAKawijZBEv0i38L0PcP2c3TiRN4nZC2Fmw1M6kbXsSeg6QVF4RqZBVO3uuwnn33HQZCglLyLujVwspDPzyN6wqiZAj69xPJdnyufbxmQmxdfKWTpCSvpCfcMs1BF0vkdDZB1ZBBDZAuOKdw4txLZCgSF2HFUNMfOy8gp5ZCN9eAep0'

bot = Bot(PAGE_ACCESS_TOKEN)

page = Page(PAGE_ACCESS_TOKEN)

@app.route('/',methods=['GET'])

def verify():
	
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        	if not request.args.get("hub.verify_token") == "hello":
            		return "Verification token mismatch", 403
        	return request.args["hub.challenge"], 200
   	return "Hello world", 200


@app.route('/',methods=['POST'])


def webhook():
	data = request.get_json()
	#log(data)

	if data['object'] == 'page':
		for entry in data['entry']:
			for  messaging_event in entry['messaging']:

				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']

				if messaging_event.get('message'):
					if 'text' in messaging_event['message']:
						messaging_text = messaging_event['message']['text']
					else:
						messaging_text = 'no text:'

					print(sender_id)

					response = "none"
					entity,value = wit_response(messaging_text)
					#print(entity)
					
					if entity ==  "greetings":
						quick_reply(sender_id)
					else:
						page.send(sender_id,"welcome")


					
					

	return "ok",200



def log(message):
	print(message)
	sys.stdout.flush()


def quick_reply(sender_id):
	quick_replies = [{'title': 'New-User', 'payload' : 'pick_action'},
					  {'title': 'Old-User', 'payload' : 'pick_action'}
	]
	page.send(sender_id,"Welcome to Kahyap-bot?",quick_replies=quick_replies,metadata ="DEVELOPER_DEFINED_METADATA")


if __name__ == "__main__":
	app.run(debug = True,port =60)
