# Twitter-Bot-Video
###### This is the repo that corresponds with my upcoming YouTube video.

# My bad for not doing this, it will get done it is just gonna take a long time cause im busy

In this project you are going to create a Twitter bot hosted in the cloud with Tweepy, Linode, and Twilio that sounds
out a tweet every day with an attached quote. Then send you a confirmation text/email
### Project status:


- [X] Create github
- [ ] Create video(s)
- [ ] Edit video
- [ ] edit github
- [ ] post video
- [ ] success and fame (or maybe just a pat on the back, hahah)

#### See the full video at:
- [Youtube link](jfcom.ca)


#### Video planning (with links to sub videos):
- [X] [Installing pycharm](youtube.com)
- [X] [Create files and enviroment](youtube.com)
- [ ] [Plan/send tweet](youtube.com)
- [ ] [Send email/text function](youtube.com)
- [ ] [Put it all together](youtube.com)
- [ ] [Load into linode](youtube.com)

# Where to start?
You should start by taking a look at the cumulative video. This will guide you through all the actual code.
If you don't know how to install and IDE (or even what in the hell that is) or how to set up an environment
start by looking at the first two smaller videos than moving forwards.
#### What do you need to know: (prerequisite knowledge)
- How to install an IDE
- How to install python on your local machine


#### In the video I go over a few things like:
- Setting up a Twitter bot
- Working with tweepy
- Getting notified of tweets
- Handling errors
- Sending texts with Twilio
- Handling json files
- Using crontab
- The bare bones of linode and VPS's in general

This project is by no means perfect, but I enjoyed making it, and I hope you can learn a little from me along the way.
Feel free to suggest changes or shoot me an email at [joshua.himmens@gmail.com](mailto:joshua.himmens@gmail.com)
or even if you want more content

## Needed links:
- [Create a Google account](https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp)
- [Create Twilio account](https://www.twilio.com/try-twilio)
- [Create a Twitter account](https://twitter.com/i/flow/signup)
- [Create a Twitter dev account](https://developer.twitter.com/en/apply-for-access)
- [Jetbrains IDE download](https://www.jetbrains.com/pycharm/)
- [Create Linode account](https://linode.com/)


## links to useful resources:

- Source of the quotes: [Github repo](https://github.com/sumanto/goodreads-quotes/blob/master/quotes.json)
- Link to tweepy docs: [Docs.tweepy.org](https://docs.tweepy.org/en/latest/index.html)
- Link to real python tweepy guide: [Real python](https://realpython.com/twitter-bot-python-tweepy/)
- Link to Twitter api docs: [Twitter.com](https://developer.twitter.com/en/docs)
- Link to learn python video: [Free Code Camp youtube video](https://www.youtube.com/watch?v=rfscVS0vtbw&t=1957s)
- Twilio docs: [Twilio](https://www.twilio.com/docs)
- Python docs: [python.org](https://docs.python.org/3/)
- Linux CLI explainer: [Explainshell.com](https://explainshell.com/)
- Linode docs: [Linode](https://www.linode.com/docs/)
- Crontab Explainer: [Linuxiac.com](https://linuxiac.com/how-to-use-cron-to-schedule-tasks-the-complete-beginners-guide/#h-cron-command-entries)


## Getting started:

This is what you need to run for the tweepy package:

    pip install tweepy
    
If you want to also use Twilio:

    pip install twilio

If you are using the pycharm IDE you won't need to use either, follow the steps shown in the video to import the modules.
## During your Twitter bot project:
- Remember you can pause to mess with the code however you want, thats half of learning
- Use the docs and the videos liberally if your unsure
- Use the video as a first step into learning some more and creating your own projects
## How to go further:
###### These are some ideas for how you could go deeper into this project
- Use dynamic data (e.g. Temp data, garden monitor)
- Have tweepy record tweets sent by your bot to a json file, so you can mass delete just the tweets sent by your bot
- Create your own version of tweepy, the Twitter API is super easy to use and create
- Send the quotes in a daily text or email
- Import this file into other scripts to use functions like sending texts/emails/qoutes
- Do something better than I did it and make your own YouTube video

If you are able to come up with some cool projects or want advice on this one feel free to shoot me an email at
[joshua.himmens@gmail.com](mailto:joshua.himmens@gmail.com)
I really enjoyed making this, and I would love nothing more than an email from somebody who actually followed along <3.
