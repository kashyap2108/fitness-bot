from app import db
from app import veg
from app import non_veg
from app import drink
from app import videos
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:kashyap@localhost/fb_bot'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://pommhsyqyqzeru:2711b3952a28db3a024f241c9fb06fb793fc0967052f60cf735c77f410ac2bb6@ec2-50-19-218-160.compute-1.amazonaws.com:5432/daocq4mn1fibj3"
db = SQLAlchemy(app)

#######Videos-List#######

videos_dict={'How to increase height !!':'https://goo.gl/e9Lyhg','Reduce Belly Fat in One Week': 'https://goo.gl/Lj9rTW',
'Home Work-Out in 5 minutes !!':'https://goo.gl/bnWJ5Z','How To get rid of man"s boobs!!':'https://goo.gl/TWvUxy',
'Fat Cutter Drink ':'https://goo.gl/Abo3kQ','How to lose weight fast !!':'https://goo.gl/4XB9VR'


}
#### Drink-Menu ####
Drink=['1 cup Milk','1 glass juice']

#### Veg-Menu ####
Veg_Breakfast=['2 Sandwiches','3 Chapatis','4 Puri and sabji','4 Idlis','1 Dosa']

Veg_Lunch_Mandatory=['1 Bowl rice','1 Bowl dal','2 Chapatis']
Veg_Lunch_Optional =['1 Plate Paneer', '1 Plate Mix-Veg','1 Plate Mushroom']

Veg_Dinner_Mandatory = ['4 Chapatis']
Veg_Dinner_Optional =['1 Plate Paneer', '1 Plate Mix-Veg','1 Plate Mushroom']



#### Non-Veg-Menu #######
Non_Veg_Breakfast=['2 boiled egg','2 Egg-Parantha','1 Bread-Omlette']

Non_Veg_Lunch_Mandatory =['1 Bowl Rice','1 Bowl Dal']
Non_Veg_Lunch_Optional =['4 Piece. Chicken','1 Fish Plate', '1 Egg Curry']

Non_Veg_Dinner_Mandatory = ['4 Chapatis']
Non_Veg_Dinner_Optional =['4 Piece. Chicken','1 Fish Plate', '1 Egg Curry']




drink_dict = {'Drink':Drink}
veg_dict ={'Breakfast':Veg_Breakfast,'Veg_Lunch_Optional':Veg_Lunch_Optional,'Veg_Lunch_Mandatory':Veg_Lunch_Mandatory,'Veg_Dinner_Optional':Veg_Dinner_Optional,'Veg_Dinner_Mandatory':Veg_Dinner_Mandatory}

non_veg_dict ={'Breakfast':Non_Veg_Breakfast,'Non_Veg_Lunch_Optional':Non_Veg_Lunch_Optional,'Non_Veg_Lunch_Mandatory':Non_Veg_Lunch_Mandatory,'Non_Veg_Dinner_Optional':Non_Veg_Dinner_Optional,'Non_Veg_Dinner_Mandatory':Non_Veg_Dinner_Mandatory}

sn=int(1)

for e in drink_dict:
	for j in drink_dict[e]:
		w=drink(sn,j,e)
		db.session.add(w)
		db.session.commit()
		sn=sn+1

sn=1

for e in veg_dict:
	for j in veg_dict[e]:
		w = veg(sn,j,e)
		db.session.add(w)
		db.session.commit()
		sn = sn+1

sn=1
for e in non_veg_dict:
	for j in non_veg_dict[e]:
		w=non_veg(sn,j,e)
		db.session.add(w)
		db.session.commit()
		sn = sn+1
		
for j in videos_dict:
	w = videos(videos_dict[j],j)
	db.session.add(w)
	db.session.commit()


