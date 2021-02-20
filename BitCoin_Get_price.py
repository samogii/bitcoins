import requests
from bs4 import BeautifulSoup
from datetime import datetime
Previos=''
while True:
    now = datetime.now()
    now=now.strftime('%H:%M:%S')
    Request=requests.get('https://api.coindesk.com/v1/bpi/currentprice/CNY.json')
    Request=Request.json()
    Get_Price=Request['bpi']['USD']['rate_float']
    if Previos != Get_Price:
        print("BitCoin Price : %s In %s"%(Get_Price,now))
        Previos=Get_Price
