from priceTracker import Tracker
from mailer import Mailer

url = "https://www.amazon.com/ASUS-Certified-i7-1355U-Graphics-UX5304VA-XS76T/dp/B0BXBR2K37/ref=sr_1_34?content-id=amzn1.sym.e333145d-c591-4f23-a7a6-158d847c777a%3Aamzn1.sym.e333145d-c591-4f23-a7a6-158d847c777a&keywords=macbook+pro+14+m1&pd_rd_r=c442ffe5-b63d-4241-81e0-16b851250de5&pd_rd_w=kkmGJ&pd_rd_wg=TpScd&pf_rd_p=e333145d-c591-4f23-a7a6-158d847c777a&pf_rd_r=3VAXJ78GB21RAKMF1S7N&qid=1706627082&sr=8-34"
headers = {
	"Accept-Language": "en-US,en;q=0.9",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
}

target_price = 200  # Assuming you have set a maximum price of $200

tracker = Tracker(amazon_url=url, headers=headers)
amazon_price = float(tracker.extract_price().strip()[1:].replace(",",""))
mailer = Mailer(
		price=amazon_price,
		link=url
	)

if amazon_price <= target_price:
	mailer.send_email()
# else:
# 	print("Price is too high!")
