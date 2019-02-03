import json
import requests
import datetime
import os
import ctypes
import sys

##  TODO:
#  Need to check for file errors etc
#  Need to handle different image types?

#  Constants
baseUrl = "https://api.nasa.gov/planetary/apod"
apodImageLoc = "apodImageToday.jpg"
apodDescLoc = "apodDescToday.txt"

#  Grab API Key
keyFile = open ("apiKey", "r")
apiKey = keyFile .read ()
keyFile .close ()

#  Determine today's date (or read it as a CLI argument)
if len (sys .argv) != 1 and \
	len (sys .argv [1]) == 10 and \
	sys .argv [1][4] == '-' and \
	sys .argv [1][7] == '-':
		todayDate = sys .argv [1]
else:
	todayDate = datetime .date .today () .isoformat ()

#  Fetch APOD data
if apiKey == "DEMO_KEY":
	theFullUrl = "%s?api_key=%s" % (baseUrl, apiKey)
else:
	theFullUrl = "%s?api_key=%s&date=%s" % (baseUrl, apiKey, todayDate)
apodRequest = requests .get (theFullUrl)
apodDescText = ""

#  Check everything is in order
if apodRequest .status_code == 200 and json .loads (apodRequest .text) ["media_type"] == "image":
	#  Extract relevant image data and prettily print it
	apodDescText += "-=-  NASA Astronomy Picture Of the Day  -=-\n"
	apodDescText += "-=>  APOD for %s\n" % todayDate
	apodDescText += "-=>  Title:  %s\n" % json .loads (apodRequest .text) ["title"]
	apodDescText += "-=>  Media type:  %s\n" % json .loads (apodRequest .text) ["media_type"]
	apodDescText += "\n-=>  Explanation:\n"
	apodDescText += "%s\n" % json .loads (apodRequest .text) ["explanation"]
	print (apodDescText)
	#  Write that text to the file
	descFile = open (apodDescLoc, "w")
	descFile .write (apodDescText)
	descFile .close ()

	#  Download the new image
	hdUrl = json .loads (apodRequest .text) ["hdurl"]
	apodImageToday = requests .get (hdUrl)
	#  Write it
	imageFile = open (apodImageLoc, "wb")
	imageFile .write (apodImageToday .content)
	imageFile .close ()
	#  Change background
	ctypes .windll .user32 .SystemParametersInfoW (20, 0, os .getcwd () + "\\" + apodImageLoc, 3)
