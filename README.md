# Twitterbot-video
###### This is the repo that corresponds with my upcoming youtube video.

In this prjoect you are going to create a twitter bot hosted in the cloud with Tweepy, Linode, and Twilio that sounds out a tweet everyday with an attached qoute. Then send you a confirmation text/email
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
- [ ] [Installing pycharm](youtube.com)
- [ ] [Create files and enviroment](youtube.com)
- [ ] [Plan/send tweet](youtube.com)
- [ ] [Send email/text function](youtube.com)
- [ ] [Put it all together](youtube.com)
- [ ] [Load into linode](youtube.com)

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

this project is by no means perfect, but I enjoyed making it and i hope you can learn a little from me along the way. Feel free to suggest changes or shoot me an email at [my email](mailto:joshua.himmens@gmail.com) or even if you want more content

## Needed links:
- [Create a Google account](https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp)
- [Create Twilio account](https://www.twilio.com/try-twilio)
- [Create a Twitter account:](https://twitter.com/i/flow/signup)
- [Create a Twitter dev account:](https://developer.twitter.com/en/apply-for-access)
- [Jetbrains IDE downlaod:](https://www.jetbrains.com/pycharm/)


## links to useful resources:

- Source of the qoutes: [Github repo](https://github.com/sumanto/goodreads-quotes/blob/master/quotes.json)
- Link to tweepy docs: [Docs.tweepy.org](https://docs.tweepy.org/en/latest/index.html)
- Link to real python tweepy guide: [Real python](https://realpython.com/twitter-bot-python-tweepy/)
- Link to Twitter api docs: [Twitter.com](https://developer.twitter.com/en/docs)
- Link to learn python video: [Free Code Camp youtube video](https://www.youtube.com/watch?v=rfscVS0vtbw&t=1957s)
- Twilio docs: [Twilio](https://www.twilio.com/docs)
- Python docs: [python.org](https://docs.python.org/3/)

## Getting started:

This is what you need to run for the tweepy package:

    pip install tweepy
    
If you want to also to use twillio:

    pip install twilio

If you are using the pycharm IDE you won't need to use either, follow the steps shown in the video to import the modules.
## During your twitter bot project:
- Rember you can pause to mess with the code however you want, thats half of learning
- Use the docs and the videos liberaly if your unsure
- Use the video as a first step into learning some more and creating your own projects
## How to go further:
###### These are some ideas for how you could go deeper into this project
- Use dynamic data (e.g. Temp data, garden monitor)
- Have tweepy record tweets sent by your bot to a json file, so you can mass delete just the tweets sent by your bot
- Create your own version of tweepy, the Twitter API is super easy to use and create
- Send the quotes in a daily text or email
- Import this file into other scripts to use functions like sending texts/emails/qoutes
- Do something better than I did it and make your own YouTube video
If you are able to come up with some cool projects or want advice on this one feel free to shoot me an email at [joshua.himmens@gmail.com](mailto:joshua.himmens@gmail.com)