import requests
from bs4 import BeautifulSoup
import smtplib

URL = "" # add the link
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.396"} # add custom headers

def send_email():
    sever=smtplib.SMTP('smtp.gmail.com',587)
    sever.ehlo()
    sever.starttls()
    sever.ehlo()

    sever.login('','') # Add credentials in the format is {user},{password}
    body=URL
    msg=f"Body:{body}\nThe price has dropped"
    sever.sendmail("","",msg)
    sever.quit()

def check_price():

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(id='priceblock_ourprice').getText()
    price=price.replace(",","")
    price=price.split('.',1)
    sub_price=price[0]
    sub_price=int(sub_price)
    print(sub_price)
    if sub_price < 2999:
        send_email()

check_price()
