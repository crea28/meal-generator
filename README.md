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
Generated 3 random meals:
Quinoa - Haricots Verts
Tomates farcies - Riz
Tortilla espagnole

Shopping List:
Chair à saucisses: 300 g
Haricots verts: 200 g
Huile d'olive: 4 cuillère(s) à soupe
Oeuf: 6 pièce(s)
Poivre: 1 pincée(s)
Pommes de terre: 500 g
Quinoa: 250 g
Riz: 300 g
Sel: 1 pincée(s)
Tomates rondes: 4 pièce(s)
```
## How to add/update a recipe ?

In order to add a new recipe with ingredients, you have to edit/update the file __recipe.json__ in adding a new bloc : 
```
        {
            "name": "Pâtes - Jambon",
            "ingredients": [
                {
                    "name": "Dés de jambon",
                    "quantity": 150,
                    "unit": "g"
                },
                {
                    "name": "Pâtes",
                    "quantity": 350,
                    "unit": "g"
                }
            ],
            "season": ["winter","automn","spring","summer"]
        },
```

Please, pay attention to the comma at the end of the block, according to the json syntax.

Under 'ingredients', here is the definition of each entry : 

- __name :__ enter here the name of the recipe
- __name :__ enter the name of the ingredient
- __quantity :__ enter here the quantity
- __unit :__ enter here g, kg, pièce(s), etc ...
- __season :__ enter here the season. For example, if you note "winter", the recipe will not be used if you are in spring, in automn or in summer. You can add multiple season.

## Final Word !

> Bon appétit !


