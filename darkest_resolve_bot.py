import praw
import config
import time
import random
import os

run = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = config.user_agent) 
			
status = ['Paranoid', 'Selfish', 'Irrational', 
		  'Fearful', 'Hopeless', 'Abusive', 
		  'Masochistic', 'Rapturous', 'Powerful',
		  'Courageous', 'Stalwart', 'Vigorous',
		  'Focused']

if not os.path.isfile("comment_list.txt"):
	comment_list = []
else:
	with open("comment_list.txt", "r") as f:
		comment_list = f.read()
		comment_list = comment_list.split("\n")
		comment_list = list(filter(None, comment_list))

print("Grabbing the last 10 comments")
for comment in run.subreddit('DarkestDungeon').comments(limit=10)
	if comment.id not in comment_list and "resolve is tested..." in comment.body:
		print("Comments found!")
		comment.reply("#" + random.choice(status))
		print("Sending message and recording comment id.")
		comment_list.append(comment.id)
			
	with open("comment_list.txt", "w") as f:
		for 
		f.write(comment.id + "\n")			
	
	print("Taking a break...")
	time.sleep(30)


run = login_reddit()
status = status_list()	
comment_list = replies_list()


while True:
	run_darkest_bot(run, status, comment_list)

