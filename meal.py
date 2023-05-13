#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

import json
import random
import sys
import datetime
from datetime import date, timedelta, datetime

# Arguments
if len(sys.argv ) != 2:
    print("\t Usage: ", sys.argv[0], "number of days, example : ", sys.argv[0], "3" )
    exit();

def get_season():
    # Get the current day of the year
    doy = datetime.today().timetuple().tm_yday

    # Day of year
    spring = range(80, 172)
    summer = range(172, 264)
    automn = range(264, 355)
    # winter = everything else

    if doy in spring:
        seasonNow = 'spring'
    elif doy in summer:
        seasonNow = 'summer'
    elif doy in automn:
        seasonNow = 'automn'
    else :
        seasonNow = 'winter'

    return seasonNow

def generate_shopping_list(file_path, num_meals, fseason):
    with open(file_path) as f:
        data = json.load(f)

    if fseason:
        num_season_available_meals = [meal for meal in data["meals"] if fseason in meal["season"]]
        num_available_meals = len(num_season_available_meals)
    else:
        num_season_available_meals = [meal for meal in data["meals"]]
        num_available_meals = len(num_season_available_meals)

    if num_meals > num_available_meals:
        print(f"{fseason} Warning: Requested {num_meals} meals, but only {num_available_meals} are available. Using all available meals.")
        exit();

    # Randomly select num_meals meals
    meals = random.sample(num_season_available_meals, num_meals)

    shopping_list = {}

    for meal in meals :
        for ingredient in meal["ingredients"]:
            name = ingredient["name"]
            quantity = ingredient["quantity"]
            unit = ingredient["unit"]
            if name in shopping_list:
                shopping_list[name]["quantity"] += quantity
            else:
                shopping_list[name] = {"quantity": quantity, "unit": unit}

    return shopping_list, [meal["name"] for meal in meals]

if __name__ == "__main__":
    file_path = "recipe.json"
    num_meals = int(sys.argv[1])
    fseason = get_season()

    shopping_list, meals = generate_shopping_list(file_path, num_meals, fseason)
    print(f"Generated {len(meals)} random meals:")
    for meal in sorted(meals):
        print("- " + meal)
    print("\nShopping List:")
    for item in sorted(shopping_list):
        print(f"{item}: {shopping_list[item]['quantity']} {shopping_list[item]['unit']}")
