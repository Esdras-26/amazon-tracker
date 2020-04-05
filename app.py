import requests
from bs4 import BeautifulSoup
import smtplib
import email.message

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}

URL = ""

price_limit = 100

mail = ""
mdp = ""


def app():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find(id="productTitle").get_text().strip()
    price = soup.find(id="priceblock_ourprice").get_text()[:-2]
    price = price[:-3] + "." + price[-2:]
    price = float(price)
    if(price <= price_limit):
        sendEmail(title)


def sendEmail(title):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(mail, mdp)

    body = 'Le prix de ' + title + ' est inférieur à ' + \
        str(price_limit) + ' Fonce ! ' + URL
    msg = email.message.Message()
    msg['Subject'] = "Baisse des PRIX "
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body)
    server.sendmail(mail, mail,
                    msg.as_string().encode("utf-8"))
    print("email send")


if __name__ == "__main__":
    app()
