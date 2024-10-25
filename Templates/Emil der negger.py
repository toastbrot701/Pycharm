import smtplib
import pandas as pd

toaddrs = 'toastbrot.hs@gmail.com'
fromaddrs = 'toastbrot.hs@gmail.com'
message = 'Hallo'

with smtplib.SMTP('smpt.gmail.com', '587') as smtpserver:
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login('toastbrot.hs@gmail.com', 'Hansi998876')
    for i in range(10):
        smtpserver.sendmail(fromaddrs, toaddrs, message)
        print(i)

