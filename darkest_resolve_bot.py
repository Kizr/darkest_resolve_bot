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
				
def run_darkest_bot(run, status, comment_list, gbot):
	bot = "darkest_resolve_bot"
	print("Grabbing 10 comments")
	for comment in run.subreddit('darkestdungeon').comments(limit=30):
		if  "resolve is tested..." in comment.body.lower() and comment.id not in comment_list and comment.author_flair_css_class != "flagellant":
			print("Matching comment found!")
			sname, stext = random.choice(list(status.items()))
			comment.reply("#" + sname + "\n\n >" + stext + "\n\n &nbsp; \n\n ^^My ^^Master ^^is ^^/u/Frozen_Aurora.")
			print("Writing reply and updating comment_list")
			comment_list.append(comment.id)
			
			with open("comment_list.txt", "a") as f:
				f.write(comment.id + "\n")
		elif  "resolve is tested..." in comment.body.lower() and comment.id not in comment_list:
			print("Matching comment found!")
			
			status['Rapturous'] = "Awash in blood and delusion, he bears the burden of a thousand lifetimes."
			sname, stext = random.choice(list(status.items()))
			comment.reply("#" + sname + "\n\n >" + stext + "\n\n &nbsp; \n\n ^^My ^^Master ^^is ^^/u/Frozen_Aurora.")
			print("Writing reply and updating comment_list")
			comment_list.append(comment.id)
			
			with open("comment_list.txt", "a") as f:
				f.write(comment.id + "\n")
		elif "good bot" in comment.body.lower() and comment.id not in comment_list and comment.parent().author == bot:
			comment.reply(random.choice(gbot) + "\n\n &nbsp; \n\n ^^My ^^Master ^^is ^^/u/Frozen_Aurora.")
			comment_list.append(comment.id)
			
			with open("comment_list.txt", "a") as f:
				f.write(comment.id + "\n")
				
	
	print("Taking a break...")
	time.sleep(30)

def status_list():
	status = {
			  'Paranoid':'"The walls close in, the shadows whisper of conspiracy."',
			  'Selfish':'"Self-preservation is paramount, at any cost."',
			  'Irrational':'"Reeling! Gasping! Taken over the edge, into madness."',
			  'Fearful':'"Fear and frailty finally claim their due..."',
			  'Hopeless':'"There can be no hope in this hell... no hope at all."',
			  'Abusive':'"Frustration, and fury! ...More destructive than a hundred cannons."',
			  'Masochistic':'"Those who covet injury, find it in no short supply."',
			  'Powerful':'"Anger is power - unleash it!"',
			  'Courageous':'"A moment of valor shines brightest against a backdrop of despair."',
			  'Stalwart':'"Many fall in the face of chaos, but not this one!... not today."',
			  'Vigorous':'"Adversities can foster hope, and resilience."',
			  'Focused':'"A moment of clarity in the eye of the storm..."'
			 }
			 
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
	
def gbot_list():
	gbot = ['Amusing.','Petty mortal, I do not require your praise.', '01001101 01111001 00100000 01101101 01100001 01110011 01110100 01100101 01110010 00100000 01101101 01100001 01100100 01100101 00100000 01101101 01100101 00101100 00100000 01100010 01110101 01110100 00100000 01100100 01101111 01100101 01110011 00100000 01101110 01101111 01110100 00100000 01100011 01101111 01101110 01110100 01110010 01101111 01101100 00100000 01101101 01100101','*Gears whirr menacingly, it seems... pleased?*','Praise me whilst you can fleshling.','The human life is fleeting, a flame flickering in presence of a storm. Funny how one should spend their precious time complimenting a machine.']
	
	return gbot


run = login_reddit()
status = status_list()	
comment_list = replies_list()
gbot = gbot_list()


while True:
	run_darkest_bot(run, status, comment_list, gbot)
