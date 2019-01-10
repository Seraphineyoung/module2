# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:00:48 2019

@author: serap
"""
import requests
#
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxaefaacd34fc64849bca7491733dadc3f.mailgun.org/messages",
        auth=("api", "a62dc14dda4d40d53881fe12e07aea79-060550c6-6a46c35e"),
        data={"from": "Exicited User <seraphine_ene@yahoo.com>",
              "to": "Seraphine <kate.sorotos@bt.com>",
              "subject": "Hello Seraphine",
              "text": "Congratulations Seraphine, you just sent an email with Mailgun!  You are truly awesome!"})
    
    
send_simple_message()



#import requests
#
#endpoint = "http://api.openweathermap.org/data/2.5/weather"
#payload = {"q": "London,UK", "units":"metric", "appid":"cbbebfc9a51d8f4c0135dded92eba31a"}
#response = requests.get(endpoint, params = payload)
#data = response.json()
#
#
#print(data)
#print('This is what data looks like: \n')
#print(response.url)
#print(response.status_code)
#print(response.headers["content-type"])



















