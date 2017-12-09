import praw
from time import sleep
import datetime

'''
account credentials
how to get these credentials on a new account:
    step 1: go to preferences
    step 2: go to the apps tab (right beside options and rss feeds)
    step 3: press "create another app"
    step 4: fill out name and description
    step 5: leave about url blank, in redirect uri put "https://reddit.com/r/all"
    step 6: select the "script button", the default will be "web app"
    step 7: press create app
    step 8: for the client id put the string of numbers and letters under "personal use script" and beside the question mark icon
    step 9: for the client secret put the string of numbers and letters beside "secret"
    step 10: for user agent put a short description of what the bot does and replace "/u/urnancx" with your name

if you have never worked with python before here is how to run this bot:
    you have 2 options: either to run the bot on a personal computer or a hoster
    to run on your personal computer you will have to set up python. To set up python look up a quick tutorial and then simply run this file by pressing f5
    the downside to running on personal computer is that you will only be able to run it when your computer is on
    if you want to host the bot i recommend www.pythonanywhere.com. It is one of the only good python hosters i have been able to find that is free. All you have to do to is sign up, upload this file, open it in pythonanywhere, and press on run.   
'''

r = praw.Reddit(client_id='79FHWP11IfBzLg', 
                     client_secret='wmfvri1U2ZBbbrcpkLH44AFSB38',
                     password='password',
                     user_agent='subreddit moderator made by /u/urnancx',
                     username='testmod-bot')


###################################################################################################
# IMPORTANT if you try to run this bot on a subreddit where it isnt modded it will return an error#
###################################################################################################

#feel free to contact me if you get any errors or are confused about anything
#or want to change anything about the bot

subreddit = r.subreddit("backtoschooldeals")
#change to subreddit you want to moderate
# you can moderate multiple subreddits at the same time by doing "backtoschooldeals + funny + pics"
while True: #loops infinitely
    for submission in subreddit.stream.submissions(): #gets all submissions from subreddit
        date = datetime.datetime.fromtimestamp(submission.created_utc) #converts timestamp of how old submission is into date
        date_mins = (datetime.datetime.now()-date).total_seconds() / 60.0 #gets how old submission is in minutes
        if date_mins > 60.0 and submission.score <= 10: #activates if score is below threshold and at least 60 minutes old. Just change the 10 to whatever score you want it to remove at. If you want to change how old the submission has to be to remove it change the 60 to however many minutes you want (must have .0 at end or will likely return float error)
            submission.mod.remove() #removes submission
