import praw
import config
import time
import random
import os

def login_reddit():
	run = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = config.user_agent) 
	return run
				
def run_darkest_bot(run, status, comment_list):
	print("Grabbing 10 comments")
	for comment in run.subreddit('DarkestDungeon').comments(limit=30):
		if  "resolve is tested..." in comment.body.lower() and comment.id not in comment_list:
			print("Matching comment found!")
			comment.reply("#" + random.choice(status) + "/n/n" + "^^I am a bot, and this action was performed automatically. Please contact /u/Frozen_Aurora if you have any questions or concerns.")
			print("Writing reply and updating comment_list")
			comment_list.append(comment.id)
			
			with open("comment_list.txt", "a") as f:
				f.write(comment.id + "\n")
				
	
	print("Taking a break...")
	time.sleep(30)
			
def status_list():
	status = ['Paranoid', 'Selfish', 'Irrational', 
			  'Fearful', 'Hopeless', 'Abusive', 
			  'Masochistic', 'Rapturous', 'Powerful',
			  'Courageous', 'Stalwart', 'Vigorous',
			  'Focused']
	return status
	
def replies_list():
	if not os.path.isfile("comment_list.txt"):
		comment_list = []
	else:
		with open("comment_list.txt", "r") as f:
			comment_list = f.read()
			comment_list = comment_list.split("\n")
			comment_list = list(filter(None, comment_list))
	
	return comment_list


run = login_reddit()
status = status_list()	
comment_list = replies_list()


while True:
	run_darkest_bot(run, status, comment_list)

