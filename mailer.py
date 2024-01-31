import smtplib
import os


class Mailer:
	def __init__(self, price, link):
		self.price = price
		self.link = link
		self.email = "patrickonodje@gmail.com"
		self.password = os.getenv("MAIL_PASSWORD")
		self.message = None

	def read_message(self):
		with open("message.txt") as f:
			lines = f.read()

		new_words = {
			"{price}": str(self.price),
			"{link}": self.link
		}

		for key in new_words.keys():
			if key in lines:
				lines = lines.replace(key, new_words[key])

		self.message = lines

		return self.message

	def send_email(self):
		message = self.read_message()
		with smtplib.SMTP("smtp.gmail.com") as connection:
			connection.starttls()
			connection.login(user=self.email, password=self.password)
			msg = f"Subject: New low price alert!\n\n{message}"
			connection.sendmail(
				from_addr=self.email,
				to_addrs=self.email,
				msg=msg.encode("utf-8")
			)
