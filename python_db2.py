from exp1 import db
from exp1 import veg
from exp1 import non_veg
from exp1 import drink
from exp1 import videos

db.create_all()

#######Videos-List#######

videos_dict={'How to increase height !!':'https://goo.gl/6NRj9y','Reduce Belly Fat in One Week': 'https://goo.gl/jmA9MW',
'Home Work-Out in 5 minutes !!':'https://goo.gl/UcTL5G','How To get rid of man"s boobs!!':'https://goo.gl/HWBF7P',
'Fat Cutter Drink ':'https://goo.gl/dXLFDf','How to lose weight fast !!':'https://goo.gl/oJALfP'


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


