#!/usr/bin/python3

from email.message import EmailMessage
import ssl
import smtplib

email_sender = input('sender: ')
email__password = input('password: ')

email_receiver = input('Receiver: ')

subject = input('Subject: ')
body = input('write the email: ')

e = EmailMessage()
e['From'] = email_sender
e['TO'] = email_receiver
e['Subject'] = subject
e.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email__password)
    smtp.sendmail(email_sender, email_receiver, e.as_string())