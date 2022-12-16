from bs4 import BeautifulSoup
from smtplib import SMTP
import requests
import os

AMAZON_INSTANT_POT = "https://www.amazon.ca/dp/B06Y1MP2PY?ref_=cm_sw_r_cp_ud_dp_KSMTX9CKEFM5XHZ2BCHQ&th=1"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9,fr;q=0.8"
}

response = requests.get(url=AMAZON_INSTANT_POT, headers=headers)

content = response.text
soup = BeautifulSoup(content, "html.parser")

price = soup.find("span", class_="a-price-whole")
price = price.text.split(".")[0]


def send_mail(email,price):
    my_email = "sereil@live.ca"
    password = None
    with SMTP("smtp-mail.outlook.com", port=587) as connection:

        '''Secure the Connection using TLS'''
        connection.starttls()

        '''Set Credentials'''
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=email,msg =f"Subject:Instant Pot Price Drop!\n\nThe Instant Pot 6Qt has dropped to {price}")

if int(price) < 100:
    send_mail(None,price)

