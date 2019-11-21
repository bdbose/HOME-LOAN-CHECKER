# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 22:18:37 2019

@author: bdbos
"""


import smtplib


def send_email(CLIENT_EMAIL,msg):
    subject = "DREAM HOUSING LOANS"
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login('YOUR EMAIL ADDRESS', 'YOUR EMAIL PASSWORD')
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail('YOUR EMAIL ADDRESS', CLIENT_EMAIL, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


    


