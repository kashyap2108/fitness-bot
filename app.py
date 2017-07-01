import os,sys
import datetime as dt
from flask import Flask,request
from utils import wit_response
import json
import requests
from pymessenger import Bot
from fbmq import Page,Attachment,Template,QuickReply
from flask_sqlalchemy import SQLAlchemy
from numpy import random

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:kashyap@localhost/fb_bot'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://pommhsyqyqzeru:2711b3952a28db3a024f241c9fb06fb793fc0967052f60cf735c77f410ac2bb6@ec2-50-19-218-160.compute-1.amazonaws.com:5432/daocq4mn1fibj3"

db = SQLAlchemy(app)

PAGE_ACCESS_TOKEN = 'EAAbYwLFXiZAABAKawijZBEv0i38L0PcP2c3TiRN4nZC2Fmw1M6kbXsSeg6QVF4RqZBVO3uuwnn33HQZCglLyLujVwspDPzyN6wqiZAj69xPJdnyufbxmQmxdfKWTpCSvpCfcMs1BF0vkdDZB1ZBBDZAuOKdw4txLZCgSF2HFUNMfOy8gp5ZCN9eAep0'
bot = Bot(PAGE_ACCESS_TOKEN)
page = Page(PAGE_ACCESS_TOKEN)


########## TABLES #########

class drink(db.Model):
	sn = db.Column(db.Integer, primary_key = True)
	id = db.Column(db.String(80))
	item = db.Column(db.String(80))

	def __init__(self,sn,item,id):
		self.sn = sn
		self.item = item
		self.id = id


class veg(db.Model):
	sn = db.Column(db.Integer, primary_key = True)
	id = db.Column(db.String(80))
	item = db.Column(db.String(80))

	def __init__(self,sn,item,id):
		self.sn = sn
		self.item = item
		self.id =id
        
        



class non_veg(db.Model):
	sn = db.Column(db.Integer, primary_key = True)
	id = db.Column(db.String(80))
	item = db.Column(db.String(80))

	def __init__(self,sn,item,id):
		self.sn = sn
		self.item = item
		self.id = id
	
	

	
class videos(db.Model):
	url = db.Column(db.String(80),primary_key = True)
	desc = db.Column(db.String(80),unique =True)

	def __init__(self,url,desc):
		self.url = url
		self.desc = desc


#############CREATE DATABASE#######

db.create_all()
#import python_db2
@app.route('/',methods=['GET'])

def verify():
	
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        	if not request.args.get("hub.verify_token") == "hello":
            		return "Verification token mismatch", 403
        	return request.args["hub.challenge"], 200
   # return "Hello world", 200
   		return "Hello world", 200


@app.route('/',methods=['POST'])


def webhook():
	data = request.get_json()
	#log(data)

	if data['object'] == 'page':
		for entry in data['entry']:
			for  messaging_event in entry['messaging']:

				sender_id = str(messaging_event['sender']['id'])
				recipient_id = str(messaging_event['recipient']['id'])
					
				if messaging_event.get('message'):


					if 'text' in messaging_event['message']:
						messaging_text = messaging_event['message']['text']
					else:
						messaging_text = 'no text:'

					#print(sender_id)

					response = "none"
					entity,value = wit_response(messaging_text)
					#print(entity)
					if entity ==  "greetings":
						quick_reply(sender_id)
					elif entity == "diet_entity":
						page.send(sender_id,"Veg or Non-Veg?")
					elif entity == "video_entity":
						send_videos(sender_id)
					elif entity =="subscribe_entity":
						page .send(sender_id,"You will get daily fitness quotes!!")
					elif entity == "diet_type":
						if value == 'veg':
							veg_diet(sender_id)
						else:
							non_veg_diet(sender_id)

					else:
						page.send(sender_id,"Please enter a valid choice!!")
						quick_reply(sender_id)


					return "ok",200


	return "ok",200


###########SEND VIDEOS##########
def send_videos(sender_id):
	w=videos.query.all()
	xyz=random.choice(w)
	#print(xyz.url)
	url=str(xyz.url)
	desc=str(xyz.desc)
	page.send(sender_id,Attachment.Video(url))
	page.send(sender_id,"desc")
	quick_reply(sender_id)


###########SEND NON-VEG-DIET ACC. To TIME###########
def non_veg_diet(sender_id):
	list=[]
	hour =dt.datetime.now().hour
	if(hour>5 and hour <12):
		w=non_veg.query.filter_by(id='Breakfast').all()
		z = w[randint(0,len(w)-1)].item
		list.append(z)

		juice=drink.query,filter_by(id='Drink').all()
		z = w[randint(0,len(juice)-1)].item
		list.append(z)

	elif(hour>12 and hour <16):
		w=non_veg.query.filter_by(id='Non_Veg_Lunch_Mandatory').all()
		for i in w:
			list.append(i.item)

		x=non_veg.query.filter_by(id='Non_Veg_Lunch_Optional').all()
		y=random.choice(x,2)

		for i in y:
			list.append(i.item)

	elif(hour>16 and hour <18):
		page.send(sender_id,"Snacks not available !!!")
		quick_reply(sender_id)
		return


	elif(hour>18 and hour<24):
		w=non_veg.query.filter_by(id="Non_Veg_Dinner_Mandatory").all()
		for i in w:
			list.append(i.item)

		x = non_veg.query.filter_by(id='Non_Veg_Dinner_Optional').all()
		y=random.choice(x,2)

		for i in y:
			list.append(i.item)

	for i in list:
		page.send(sender_id,i)

	quick_reply(sender_id)


###########SEND VEG-DIET ACC. To TIME###########

def veg_diet(sender_id):
	list=[]
	hour =dt.datetime.now().hour
	if(hour>5 and hour <12):
		w=veg.query.filter_by(id='Breakfast').all()
		z = w[randint(0,len(w)-1)].item
		list.append(z)

		juice=drink.query,filter_by(id='Drink').all()
		z = w[randint(0,len(juice)-1)].item
		list.append(z)

	elif(hour>12 and hour <16):
		w=veg.query.filter_by(id='Veg_Lunch_Mandatory').all()
		for i in w:
			list.append(i.item)

		x=veg.query.filter_by(id='Veg_Lunch_Optional').all()
		y=random.choice(x,2)

		for i in y:
			list.append(i.item)
	

	elif(hour>16 and hour <18):
		page.send(sender_id,"Snacks not available !!!")
		quick_reply(sender_id)
		return


	elif(hour>18 and hour<24):
		w=veg.query.filter_by(id="Veg_Dinner_Mandatory").all()
		for i in w:
			list.append(i.item)

		x = veg.query.filter_by(id='Veg_Dinner_Optional').all()
		y=random.choice(x,2)

		for i in y:
			list.append(i.item)

	for i in list:
		page.send(sender_id,i)

	quick_reply(sender_id)






def quick_reply(sender_id):
	quick_replies = [{'title': 'Get Your Diet', 'payload' : 'pick_action'},
					  {'title': 'Fitness-Videos', 'payload' : 'pick_action'},
					  {'title': 'Subscribe ', 'payload' : 'pick_action'}
	]
	page.send(sender_id,"Welcome to Diet-Bot !!!",quick_replies=quick_replies,metadata ="DEVELOPER_DEFINED_METADATA")


if __name__ == "__main__":
	app.run(debug = True,port=50)
