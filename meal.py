#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# Carbohydrates (glucides) : potatoes, pasta, rice, legumes, pizza bases or wholegrains such as barley, buckwheat or quinoa.

import json
import random
import calendar
import datetime
from datetime import date, timedelta

tmpArray = []
recipeArray = []
tmpIngMeat = []
tmpIngVegetables = []
tmpIngCheese = []
tmpIngFish = []
tmpIngFrozenFood = []
tmpIngCarbohydrates = []
tmpIngOthers = []

# Load json file
f=open('recipe.json')
data = json.load(f)

# Get the recipe list
for i in data['recipe']:
    recipeArray.append(i['title'])

# Close json file
f.close()

for days in range(15):
    NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=days)
    NextDay_Date_formatted = NextDay_Date.strftime ('%a %d %B %Y')

    countTotal = str(len(recipeArray))
    if countTotal != "0":
        rand=random.choice(recipeArray)
        tmpArray.append(rand)
        recipeArray.remove(rand)
        print NextDay_Date_formatted, ":", rand

        # Get all the ingredients
        for i in data['recipe']:
            if rand == i['title']:
                if len(i['ing_meat']) != 0: tmpIngMeat.append(i['ing_meat'])
                if len(i['ing_vegetables']) != 0: tmpIngVegetables.append(i['ing_vegetables'])
                if len(i['ing_cheese']) != 0: tmpIngCheese.append(i['ing_cheese'])
                if len(i['ing_fish']) != 0: tmpIngFish.append(i['ing_fish'])
                if len(i['ing_frozen_food']) != 0: tmpIngFrozenFood.append(i['ing_frozen_food'])
                if len(i['ing_carbohydrates']) != 0: tmpIngCarbohydrates.append(i['ing_carbohydrates'])
                if len(i['ing_others']) != 0: tmpIngOthers.append(i['ing_others'])

    else :
        print NextDay_Date_formatted, ": Regime"

print "\n\t ## Legumes"
for x in tmpIngVegetables:
    print json.dumps(x, default=str).decode('unicode-escape')[1:-1]

print "\n\t ## Viandes"
for x in tmpIngMeat:
    print json.dumps(x, default=str).decode('unicode-escape')[1:-1]

print "\n\t ## Fromage"
for x in tmpIngCheese:
    print json.dumps(x, default=str).decode('unicode-escape')[1:-1]

print "\n\t ## Poissons"
for x in tmpIngFish:
    print json.dumps(x, default=str).decode('unicode-escape')[1:-1]

print "\n\t ## Surgelés"
for x in tmpIngFrozenFood:
    print json.dumps(x, default=str).decode('unicode-escape')[1:-1]

print "\n\t ## Glucides"
for x in tmpIngCarbohydrates:
    print json.dumps(x, default=str).decode('unicode-escape')[1:-1]

print "\n\t ## Autres"
for x in tmpIngOthers:
    print json.dumps(x, default=str).decode('unicode-escape')[1:-1]