# BBDC

How it works:
- The bot will login and refresh the booking page until a slot is found.
- When a slot is found and booked, your computer will make a sound.
- To continue to look for and book slots, you will have to re-run the programme.
- The programme can run in the background while you do other things with you computer/leave on idle

##Prerequisites:

You will have to download/install the following:

1. Google Chrome
2. Chromedriver https://chromedriver.chromium.org/downloads
3. Python 

##Config:

Open the bbdc_bot.py file with your favourite IDE and change these following lines of code:

chromedriver_location in line 5 with the path of your chromedriver that you had downloaded
username and password in lines 7 and 8
required months (line 15),sessions (line 19) days (line 23), and slots (line 25). These are all lists that contain all of the various options that you see in the UI, with elements in chronological order (first month is months[0], second is months[1], etc.)
