#!/usr/bin/python3
from sense_hat import SenseHat
import smtplib
import ssl
import email
from dotenv import load_dotenv, find_dotenv
import os
from datetime import datetime


def load_args():
	load_dotenv(find_dotenv())
	GMAIL = os.environ.get("GMAIL")
	port = 465  # For SSL
	#password = input("Type your password and press enter: ")
	sender_email = "bunkuhome@gmail.com"
	receiver_email = input("Send email to: ")
	now = datetime.now().strftime("%y-%m-%d %H:%M:%S")
	subject = f"Subject: Bunkuhome stats at {now}\n"
	signature = "\n\nsent to you with love from raspberry"
	return port, GMAIL, sender_email, receiver_email, subject, signature
	

def get_temp():
	print("get_temp was called")
	string = '\nThe current temperature in Bunkuhome is: '
	sense = SenseHat()
	sense.clear()
	temp = sense.get_temperature()
	print(f"returning {string + str(round(temp, 2))}*C")
	return string + str(round(temp, 2)) + "*C"
	
def get_hum():
	print("get_hum was called")
	string = '\nThe current humidity in Bunkuhome is: '
	sense = SenseHat()
	hum = sense.get_humidity()
	print(f"returning {string + str(round(hum, 2))} %")
	return string + str(round(hum, 2)) + " %"

def send_mail(port, 
			password,  
			receiver_email,
			message,
			sender_email = "bunkuhome@gmail.com"):
	# Create a secure SSL context
	context = ssl.create_default_context()

	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)

if __name__ == '__main__':
	# get email stuff
	port, GMAIL, sender_email, receiver_email, subject, signature = load_args()
	
	message = get_temp() + get_hum()
	
	send_mail(port=port, 
			password=GMAIL, 
			receiver_email=receiver_email,
			message=subject+message+signature)
	print(f"email sent to {receiver_email}")
	print(f"final message: {subject+message+signature}")
