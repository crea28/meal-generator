#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# Carbohydrates (glucides) : potatoes, pasta, rice, legumes, pizza bases or wholegrains such as barley, buckwheat or quinoa.

import json
import random
import calendar
import datetime
from datetime import date, timedelta
import sys 

if len( sys.argv ) != 2:
    print("\t Usage: ", sys.argv[0], "number of days, exemple : ", sys.argv[0], "3" )
    exit();

numberDays = int(sys.argv[1])

tmpArray = []
recipeArray = []
tmpIngMeat = []
tmpIngPorkMeat = []
tmpIngChickenMeat = []
tmpIngBeefMeat = []
tmpIngVegetables = []
tmpIngCheese = []
tmpIngFish = []
tmpIngFrozenFood = []
tmpIngCarbohydrates = []
tmpIngOthers = []
tmpIngEggs = []
tmpIngRice = []

# Load json file
f=open('recipe.json')
data = json.load(f)

# Get the recipe list
for i in data['recipe']:
    recipeArray.append(i['title'])

# Close json file
f.close()

for days in range(numberDays):
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
                if len(i['ing_beef_meat']) != 0: tmpIngBeefMeat.append(i['ing_beef_meat'])
                if len(i['ing_chicken_meat']) != 0: tmpIngChickenMeat.append(i['ing_chicken_meat'])
                if len(i['ing_ham_meat']) != 0: tmpIngPorkMeat.append(i['ing_ham_meat'])
                if len(i['ing_rice']) != 0: tmpIngRice.append(i['ing_rice'])
                if len(i['ing_vegetables']) != 0: tmpIngVegetables.append(i['ing_vegetables'])
                if len(i['ing_cheese']) != 0: tmpIngCheese.append(i['ing_cheese'])
                if len(i['ing_fish']) != 0: tmpIngFish.append(i['ing_fish'])
                if len(i['ing_frozen_food']) != 0: tmpIngFrozenFood.append(i['ing_frozen_food'])
                if len(i['ing_carbohydrates']) != 0: tmpIngCarbohydrates.append(i['ing_carbohydrates'])
                if len(i['ing_others']) != 0: tmpIngOthers.append(i['ing_others'])
                if len(i['ing_eggs']) != 0: tmpIngEggs.append(i['ing_eggs'])
    else :
        print NextDay_Date_formatted, ": Regime"

print "\n\t ## Legumes"
for x in tmpIngVegetables:
    print json.dumps(x, default=str).decode('unicode-escape')[1:-1]

sum = 0
for x in tmpIngRice:
    rice = json.dumps(x, default=str).decode('unicode-escape')[1:-1]
    sum += int(rice)
print 'Riz : ', sum, 'g'

print "\n\t ## Viandes"
for x in tmpIngMeat:
    print json.dumps(x, default=str).decode('unicode-escape')[1:-1]

sum = 0
for x in tmpIngPorkMeat:
    ham = json.dumps(x, default=str).decode('unicode-escape')[1:-1]
    sum += int(ham)
print 'Jambon : ', sum, 'g'

sum = 0
for x in tmpIngBeefMeat:
    beef = json.dumps(x, default=str).decode('unicode-escape')[1:-1]
    sum += int(beef)
print 'Boeuf : ', sum, 'g'

sum = 0
for x in tmpIngChickenMeat:
    chicken = json.dumps(x, default=str).decode('unicode-escape')[1:-1]
    sum += int(chicken)
print 'Poulet : ', sum, 'g'

print "\n\t ## Fromage"
for x in tmpIngCheese:
    print json.dumps(x, default=str).decode('unicode-escape')[1:-1]

print "\n\t ## Poissons"
for x in tmpIngFish:
    print json.dumps(x, default=str).decode('unicode-escape')[1:-1]

print "\n\t ## Surgelés"
for x in tmpIngFrozenFood:
    print json.dumps(x, default=str).decode('unicode-escape')[1:-1]

sum = 0
for x in tmpIngCarbohydrates:
    carbohydrates = json.dumps(x, default=str).decode('unicode-escape')[1:-1]
    sum += int(carbohydrates)
print 'Pâtes : ', sum, 'g'

#print "\n\t ## Oeufs"
sum = 0
for x in tmpIngEggs:
    egg = json.dumps(x, default=str).decode('unicode-escape')[1:-1]
    sum += int(egg)
print 'Oeufs :', sum

print "\n\t ## Autres"
for x in tmpIngOthers:
    print json.dumps(x, default=str).decode('unicode-escape')[1:-1]
