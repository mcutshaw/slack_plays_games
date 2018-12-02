from slackclient import SlackClient
import os
import time
from evdev import UInput, ecodes as e

ui = UInput()


def press(key):
	waittime = .1
	ui.write(e.EV_KEY, key, 1)
	ui.syn();
	time.sleep(waittime)
	ui.write(e.EV_KEY, key, 0)
	ui.syn();


users = {}

channel_str = 'CEGA7CWC8'
slack_token = "xoxb-31574398614-493282812389-Dc0KqCOnM63zrbsixcNKLcjU"
sc = SlackClient(slack_token)
direction = 0
counter = 0
interval = 30
messages = 2
if sc.rtm_connect():
	while sc.server.connected is True:
		for event in sc.rtm_read():
			if 'text' in event.keys() and 'channel' in event.keys() and event['channel'] == channel_str:
				user = event['user']
				if user not in users.keys():
					users[user] = 0
				else:
					if users[user] > messages:
						continue
				text = event['text']
				if text == 'up':
					press(e.KEY_UP)
					if direction != 0:
						press(e.KEY_UP)
						direction = 0;
				elif text == 'down':
					press(e.KEY_DOWN)
					if direction != 2:
						press(e.KEY_DOWN)
						direction = 2;
				elif text == 'left':
					press(e.KEY_LEFT)
					if direction != 3:
						press(e.KEY_LEFT)
						direction = 3;
				elif text == 'right':
					press(e.KEY_RIGHT)
					if direction != 1:
						press(e.KEY_RIGHT)
						direction = 1;
				elif text == 'a':
					press(e.KEY_A)
				elif text == 'b':
					press(e.KEY_B)
				elif text == 'select':
					press(e.KEY_E)
				elif text == 'start':
					press(e.KEY_Q)
		counter+=1
		if counter % interval:
			for key in users.keys():
				users[key] = 0
