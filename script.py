#!/usr/bin/python
from sense_hat import SenseHat


sense = SenseHat()

def show_msg(msg):
	while True:
		sense.show_message(msg)
	
if __name__ == '__main__':
	show_msg('Hello World')
