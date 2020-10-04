import requests
import string
import random
import time
import sys
import os
import pickle
from generator.objects import Session, ResponseClass

def response_to_file(response, filename):

	with open(f"{filename}.resp", 'wb') as writer:

		pickle.dump(response, writer)


def gathering_account_data(account_data, namelength=7):

	for key in account_data:

		if "name" in key.lower():

			if key == "displayName":
				name_replacement = "".join([random.choice(string.ascii_lowercase+string.digits) for x in range(namelength+random.randint(-1,1))])

			else:
				name_replacement = "".join([random.choice(string.ascii_lowercase) for x in range(namelength+random.randint(-2,2))])

			account_data[key] = name_replacement

		elif "email" == key.lower():

			email_name = account_data["displayName"]
			account_data[key] = email_name + "@gmail.com"

	return account_data

def run():

	sesh = Session()
	responses = ResponseClass()

	epic_resp = sesh.epic()
	responses.epic = epic_resp
	response_to_file(responses, "responses")

	sesh.js()

	rep_resp = sesh.reputation()
	responses.reputation = rep_resp
	response_to_file(responses, "responses")

	loc_resp = sesh.location()
	responses.location = loc_resp
	response_to_file(responses, "responses")

	auth_resp = sesh.authenticate()
	responses.authenticate = auth_resp
	response_to_file(responses, "responses")

	merch_resp = sesh.merchantpool()
	responses.merchantpool = merch_resp
	response_to_file(responses, "responses")

	csrf_resp = sesh.csrf()
	responses.csrf = csrf_resp
	response_to_file(responses, "responses")

	analytic_resp = sesh.analytics()
	responses.analytics = analytic_resp
	response_to_file(responses, "responses")

	csrf_resp = sesh.csrf()
	responses.csrf2 = csrf_resp
	response_to_file(responses, "responses")
	
	account_data = {
					
					"country":"NL",
					"name":"",
					"lastName":"",
					"displayName":"",
					"email":"",
					"password":"Zyfer12"
					}
	account_data = gathering_account_data(account_data)
	print(account_data)
	account_resp = sesh.account(account_data)
	responses.account = account_resp

	response_to_file(responses, "responses")
