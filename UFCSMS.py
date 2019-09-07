import requests
import urllib.request
import time
import bs4
import os
from twilio.rest import Client

account_sid = "ACcdbb732b95d6283b505e8256285fe614"
auth_token = "a9a857438da22f3b120e46d213866e55"

client = Client(account_sid, auth_token)

res = requests.get('https://www.ufc.com/events')
soup = bs4.BeautifulSoup(res.text, 'lxml')

for allfightinfo in soup.find_all('div', class_='c-card-event--result__info'):

    try:  
        headline = allfightinfo.h3.a.text
        date = allfightinfo.div.a.text
        print('Next MMA: ')
        print(' ')
        print(headline)
        print(date)
        print(' ')
        break
    except:
        print("Error has occured")
        break

message = client.messages.create(
    to='+447590227798',
    from_="+441274288193",
    body=('Next MMA Fight: ' + headline + ', ' + date)
)





    

    




    

        

