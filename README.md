# Automated Lesson Booking Bot (Bukit Batok Driving Center)

This was a small project born from the frustration of the lack of driving lesson slots. This is a very simple web-scraping bot that utilizes Selenium.
This probably won't work properly anymore due to changes to the lesson booking website for BBDC, and will require some changes.


## How it works:
- The bot will login and refresh the booking page until a slot is found.
- When a slot is found and booked, your computer will make a sound.
- To continue to look for and book slots, you will have to re-run the programme.
- The programme can run in the background while you do other things with you computer/leave on idle

## Prerequisites:

You will have to download/install the following:

1. Google Chrome
2. Chromedriver (go to https://chromedriver.chromium.org/downloads download based on your version of chrome p.s. google how to check you chrome version)
4. Python (go to: https://www.python.org/downloads/)
5. Selenium (read documentation on how to download: https://selenium-python.readthedocs.io/installation.html)
6. Anaconda Navigator (https://docs.anaconda.com/anaconda/install/)

## How to run:
1. Open Anaconda Navigator
2. Launch CMD.exe Prompt
3. Type "cd Downloads" into the pop up window and press "Enter"
4. type "bbdc.py" and press enter, the code should run

## Config:

Open the bbdc_bot.py file with your favourite IDE and change these following lines of code:

chromedriver_location in line 5 with the path of your chromedriver that you had downloaded
username and password in lines 7 and 8
required months (line 15),sessions (line 19) days (line 23), and slots (line 25). These are all lists that contain all of the various options that you see in the UI, with elements in chronological order (first month is months[0], second is months[1], etc.)
