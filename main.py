import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

FROM_EMAIL = os.environ['FROM_EMAIL']
PASSWORD = os.environ['PASSWORD']
PRODUCT_URL = "https://www.amazon.com/Arae-Stretchy-Compatible-Comfortable-Adjustable/dp/B092H9Q7KY/ref=sr_1_1_sspa?crid=3PLSM5830VTYN&keywords=apple%2Bwatch%2Bband&qid=1646895419&sprefix=apple%2Bwatch%2Bban%2Caps%2C506&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyTzZQMUxDV0lGWU5UJmVuY3J5cHRlZElkPUEwNTM2ODY0MjRUQUdZMllWOVJLSCZlbmNyeXB0ZWRBZElkPUEwNTA5ODg3MzM2WFU3NUtZM1ZFSyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"

}

res = requests.get(PRODUCT_URL, headers=headers).text
soup = BeautifulSoup(res, "lxml")


main_div = soup.find(name="div", id="apex_desktop")
mid_div = main_div.find(name="div", id="corePrice_desktop")
price = float(mid_div.find(name="span", class_="a-offscreen").getText().split("$")[1])


if price < 10:
    title = soup.find(name="span", id="productTitle").getText()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=FROM_EMAIL, to_addrs="nilakshinavoda97@gmail.com",
                            msg=f"Subject:Amazon Price Alert\n\n{title} is now ${price}\n{PRODUCT_URL}")








