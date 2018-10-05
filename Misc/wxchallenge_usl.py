#!/usr/bin/env python

# import stuff
import urllib, re, calendar, time

# misc prep
now = time.gmtime() # set year to this year; needed for baseTime
baseTime = calendar.timegm((int(time.strftime("%Y", now)),1,1,0,0,0,0,0,0))
print ("")
print time.strftime("%d/%m/%Y %H:%M")
nowTime = calendar.timegm((int(time.strftime("%Y", now)), int(time.strftime("%m", now)), int(time.strftime("%d", now)), int(time.strftime("%H", now)), int(time.strftime("%M", now)),0,0, 0,0))

### Step 1: Process the raw data ###############################################

# open Microclimates /wxchallenge
raw = urllib.urlopen("http://www.microclimates.org/wxchallenge/" + time.strftime("%Y%m%d"))
print ("")
print (":::File downloaded...now processing data:::")
print ("")

### Step 2: Ask for the station ID ##############################################

city = raw_input("Which city would you like USL data for? (Enter station ID in all caps, e.g. KCAR) ")
print ("")

### Step 3: Print out desired data! ##############################################

for line in raw:
	if line[:4] == city[:4]:
		print (line)
