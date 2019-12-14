import json

def numero_destinataire(num_expediteur):

	num_expediteur = num_expediteur[4:]

	with open('correspondance.json') as myfile:
		obj = json.loads(myfile.read())

	return  obj[0][num_expediteur]