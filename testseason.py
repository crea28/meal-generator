#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys 
import json
import random
import calendar
import datetime
from datetime import date, timedelta, datetime
#from datetime import date, datetime

recipeArray = []

# get the current day of the year
doy = datetime.today().timetuple().tm_yday

# "day of year"
spring = range(80, 172)
summer = range(172, 264)
automn = range(264, 355)
# winter = everything

if doy in spring:
   seasonNow = 'spring'
elif doy in summer:
   seasonNow = 'summer'
elif doy in automn:
   seasonNow = 'automn'
else :
   seasonNow = 'winter'

print "Season :", seasonNow

# Load json file
f=open('recipe.json')
data = json.load(f)

# Get the recipe list
for i in data['recipe']:
   if seasonNow in i['season']:
      recipeArray.append(i['title'])
    
# Close json file
f.close()

countTotal = str(len(recipeArray))

print "Total :", countTotal