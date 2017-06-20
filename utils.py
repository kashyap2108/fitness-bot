from wit import Wit

access_token = "PFKRUI3H6P7LUTTNM2TWIJVYH7OUDKMA"

client = Wit(access_token = access_token)

def wit_response(message_text):
	resp=client.message(message_text)
	entity = None
	value = None
	try :
		entity = list(resp['entities'])[0]
		value = resp['entities'][entity][0]['value']
	except:
		pass
	return(entity,value)



