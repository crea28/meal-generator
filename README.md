# meal-generator

## Disclaimer 
This script is working but always in progress. It's just for fun.

All recipes and ingredients are written in French.

The ingredients are mentioned according to the way the products are bought (packaging, organic market, weight, etc.). This may differ depending on your habits and possibilities.

The script output is ugly, I'm working on it ;)

## What is meal-generator ?

This script allows to randomly generate a menu for several days in the week, the shopping list according to the season (summer, autumn, winter, spring).

It is based on an external json file containing the recipes as well as all the ingredients needed to prepare the meal.

To execute the script, simply run the following command:

> ./meal x 

__x__ is the number of meals you want to generate. For example :

```
./meal.py 3 
Fri 03 March 2023 : Oeufs sur le plat
Sat 04 March 2023 : Gauffres pomme de terre
Sun 05 March 2023 : Hamburger maison - Nuggets - Frites

	 ## Legumes
"400g pommes de terre"
"1 tomate", "Feuille de salade", "Pommes de terre à frites"
Riz :  0 g

	 ## Viandes
2x steak hachés
Jambon :  0 g
Boeuf :  0 g
Poulet :  0 g

	 ## Fromage
Cheddar
1 sachet(s) de gruyère (75g)

	 ## Poissons

	 ## Surgelés
"Nuggets", "Frites Micro-onde"
Pâtes :  0 g
Oeufs : 4

	 ## Autres
"150G de farine", "90ml de lait", "huile d'olive", "levure chimique"
"2x Pain a burger"
0 boîte(s) de crème liquide/épaisse (25cl)

```
## How to add/update a recipe ?

In order to add a new recipe with ingredients, you have to edit/update the file __recipe.json__ in adding a new bloc : 
```
{
            "title": "Riz Loc Lac",
            "ing_beef_meat": "300",
            "ing_ham_meat": "",
            "ing_bacon_meat": "",
            "ing_chicken_meat": "",
            "ing_meat": "",
            "ing_rice": "400",
            "ing_vegetables":["1 concombre", "2 tomates"],
            "ing_cheese":"",
            "ing_fish":"",
            "ing_frozen_food":"",
            "ing_carbohydrates": "",
            "ing_others":"",
            "ing_eggs": "3",
            "ing_grated_cheese": "",
            "ing_fresh_cream": "",
            "weblink": "",
            "recipe": "",
            "persons": "4",
            "season": ["winter","automn","spring","summer"]
        },
```

Please, pay attention to the comma at the end of the block, according to the json syntax.

Here is the definition of each entry : 

- __title :__ enter here the name of the recipe
- __ing_beef_meat :__ enter here the weight of beef meat in grams
- __ing_ham_meat :__ enter here the weight of ham meat in grams
- __ing_bacon_meat :__ enter here the weight of rice in grams
- __ing_chicken_meat :__ enter here the weight of chicken meat in grams
- __ing_meat :__ enter here a list
- __ing_rice :__ enter here the weight of rice needed in grams
- __ing_vegetables :__ enter here a list of vegetables
- __ing_cheese :__ enter here a list
- __ing_fish :__ enter here a list
- __ing_frozen_food :__ enter here a list
- __ing_carbohydrates :__ enter here the weight of carbohydrates in grams
- __ing_others :__ enter here a list
- __ing_eggs :__ enter here the number of eggs needed
- __ing_grated_cheese :__ enter here the number of bags (75 grams) you need
- __ing_fresh_cream :__ enter here the number of bottle (25 cl) you need
- __weblink :__ enter here a link to the recipe (youtube, etc ...). It's just an indication
- __recipe :__ enter here the description of the recipe. It's just an indication
- __persons :__ enter here the number of persons. It's just an indication
- __season :__ enter here the season. For example, if you note "winter", the recipe will not be used if you are in spring, in automn or in summer.

## T0D0
- Integrate the "season" stuff
- Complete recipe with the good ingredients
- Add some new recipes

## Final Word !

> Bon appétit !


