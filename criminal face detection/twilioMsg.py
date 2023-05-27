# -*- coding: utf-8 -*-
"""
Created on Sat May 28 02:45:55 2022

@author: asus
"""

from twilio.rest import Client
from datetime import datetime

def sendMsg(name):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    msg = name + " has been spotted at " + current_time + " in live cam "
    account_sid = "AC3e00d8b3b66438bc3ddcec8cf697ab19"
    auth_token  = "59d0e8794ed4684507fd2aef6412140b"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+916398424869", 
        from_="+12526756539",
        body= msg)
    
    print(message.sid)

