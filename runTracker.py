import sys
from phonenumbers import numbersDict
from pizzapi import *
import time
from twilio_auth import client, twilio_number

def send_text_alert(name, number, order_info):
	text_body = ''
	text_body += name + '\n'
	text_body += number + '\n'
	text_body += str(order_info['OrderDescription']) + '\n'
	text_body += 'Started at: ' + str(order_info['StartTime'])
	client.messages.create(to='+1' + str(number), from_=twilio_number, body=text_body)

if __name__ == "__main__":
	print('''Dominos (R) pizza tracker + Notifications.''')
	while True:
		for number in numbersDict:
			name = numbersDict[number]
		
			order_info = track_by_phone(number)
	
			if not order_info:
				print('No Orders Found for %s' % name)
			else:
				print(name)
				print(order_info['OrderDescription'])
				if order_info['StartTime']: print('The pizza is being made! %s' % order_info['StartTime'])
				if order_info['OvenTime']: print('The pizza is in the oven! %s' % order_info['OvenTime'])
				if order_info['RackTime']: print('The pizza is done and awaiting delivery! %s' % order_info['RackTime'])
				if order_info['RouteTime']: print('The pizza is on the way! %s' % order_info['RouteTime'])
				if order_info['DeliveryTime']: print('Your pizza was delivered! %s' % order_info['DeliveryTime'])
				send_text_alert(name, number, order_info)
			print('\n\n\n')
		time.sleep(60*30)
