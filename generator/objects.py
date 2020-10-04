import requests
import json
import string
import random
import datetime
import sys

class Session():

	def __init__(self):

		self.session = requests.Session()

		now = datetime.datetime.now()
		self.session.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51",
						'accept': "application/json, text/plain, */*"}

	def epic(self):

		url = "https://www.epicgames.com/id/register/epic"
		response = self.session.get(url)

		return response

	def js(self):

		urls = ["https://static-assets-prod.unrealengine.com/account-portal/static/static/js/2.be4a6012.chunk.js", "https://static-assets-prod.unrealengine.com/account-portal/static/static/js/main.9e031095.chunk.js", "https://tracking.epicgames.com/tracking.js"]
		
		for url in urls:

			self.session.headers.update({'referer': "https://www.epicgames.com/"})
			response = self.session.get(url)

	def reputation(self):

		url = "https://www.epicgames.com/id/api/reputation"
		self.session.headers.update({'referer': "https://www.epicgames.com/id/register/epic"})
		response = self.session.get(url)

		return response	

	def location(self):

		url = "https://www.epicgames.com/id/api/location"
		#headers.update({"cache-etag": "eyJhIjoiaHR0cHM6Ly93d3cuZXBpY2dhbWVzLmNvbSIsImIiOmZhbHNlLCJkIjpmYWxzZSwiZSI6ZmFsc2UsImYiOlsibmwiLCJlbiIsImVuLUdCIiwiZW4tVVMiXSwiZyI6IjIwMjAtMDktMjZUMDk6MjM6MzEuODIzWiIsImgiOjIsImkiOiI0OGExYmQ0Zjc1ZTQ1In0="})
		response = self.session.get(url)

		return response

	def authenticate(self):

		url = "https://www.epicgames.com/id/api/authenticate"
		response = self.session.get(url)

		return response

	def merchantpool(self):

		cooks = self.session.cookies.get_dict()
		sesh_id = cooks["EPIC_SESSION_ID"]
		
		url = f"https://merchantpool1.epicgames.com/mdt.js?session_id={sesh_id}&instanceId=9beb2fb5-b48a-4e70-a642-710892b18701&pageid=su;"
		response = self.session.get(url)

		url = f"https://merchantpool1.epicgames.com/?session_id={sesh_id}&CustomerId=9beb2fb5-b48a-4e70-a642-710892b18701&PageId=su;&w=8D862F28FD195A1&mdt=1601217319002&rticks=1601217320741"
		response = self.session.get(url)

		return response

	def ca(self):

		url = "https://epic-games-api.arkoselabs.com/fc/ca/"
		data = {"sid": "eu-west-1",
				"session_token": "3095f6e0947b28cc8.5212482605",
				"game_token": "1225f6e09d6639537.6535721205",
				"guess": {"ct":"No2Rgq8vxUE7cEIfN6dDuKdIrC71p6tjhpnLgWSp2VRf82OMR2aSil5SIcNMXXMKt6D69aKiky04+TODpyOzKccxClDL2aL2G+VqjluhW+cGNZIIYcEPFN4kiLIDPWxc2FBZe6H4DL13qy0QS6aE34YkcXdSEN0HcENdRgXaaaFDisrjogS1lf0tBmT0/C6SzbJqCDhzzNLzJ1koYB5G9nHCE/nFVdTuq7nA5e1xndM=","iv":"05e208cfaf73b50895986c257867f127","s":"99c4cf02b318fa54"},
				"analytics_tier": 40}

		response = self.session.post(url, data=data)

		return response

	def csrf(self):

		self.session.headers.update({"x-epic-event-action": "register", "x-epic-event-category": "register", "x-epic-strategy-flags": "guardianEmbeddedDocusignEnabled=true;guardianKwsFlowEnabled=false;minorPreRegisterEnabled=false;guardianEmailVerifyEnabled=false", "x-requested-with": "XMLHttpRequest"})
		url = "https://www.epicgames.com/id/api/csrf"
		response = self.session.get(url)


		return response

	def analytics(self):

		cooks = self.session.cookies.get_dict()
		xsrf_token = cooks["XSRF-TOKEN"]

		print(f"token: {xsrf_token}")

		data = {"eventType":"ACCOUNT_REGISTER_EPIC_OPEN"}
		url = "https://www.epicgames.com/id/api/analytics"

		self.session.headers.update({"x-xsrf-token": xsrf_token})
		response = self.session.post(url, data=json.dumps(data))

		return response

	def verify(self, value):

		url = "https://www.epicgames.com/id/api/verify"
		payload = {"verificationCode": str(value)}
		response = self.session.post(url, data=json.dumps(payload))
	

		return response

	def account(self, data):

		cookie_obj = requests.cookies.create_cookie(domain='www.epicgames.com',name='EPIC_COUNTRY',value='NL')
		self.session.cookies.set_cookie(cookie_obj)

		cooks = self.session.cookies.get_dict()
		xsrf_token = cooks["XSRF-TOKEN"]

		print(f"token: {xsrf_token}")

		url = "https://www.epicgames.com/id/api/account"
		self.session.headers.update({"x-xsrf-token": xsrf_token, 'accept-language': "nl", 'cookie': "EPIC_COUNTRY=NL"})

		response = self.session.post(url, data=json.dumps(data))

		print(response.text)

		return response

class ResponseClass():

	def __init__(self):

		self._created = datetime.datetime.now().strftime("%A %d. %B %Y %T")

	def __setattr__(self, name, value):

		if name != "_size" and name != "_attributes":

			self.__dict__[name] = value
			self._size = sys.getsizeof(self)
			self._attributes = []

			for attribute in dir(self):

				if attribute[0] != "_":
					self._attributes.append(attribute)

		else:
			self.__dict__[name] = value

