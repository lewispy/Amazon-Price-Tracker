import requests
from bs4 import BeautifulSoup


class Tracker:
	def __init__(self, amazon_url, headers):
		self.url = amazon_url  # Your amazon URL
		self.headers = headers
		self.response = requests.get(
			url=self.url,
			headers=self.headers,
		).text
		self.soup = BeautifulSoup(
			self.response,
			"html.parser"
		)

	def extract_price(self):
		price = self.soup.select("tr td span")[1].text
		return price
