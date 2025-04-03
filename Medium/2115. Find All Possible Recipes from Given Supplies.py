"""
You have information about n different recipes. You are given a string array
recipes and a 2D string array ingredients. The ith recipe has the name
recipes[i], and you can create it if you have all the needed ingredients from
ingredients[i]. A recipe can also be an ingredient for other recipes, i.e.,
ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that
you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer
in any order.

Note that two recipes may contain each other in their ingredients.

Constraints:
- n == recipes.length == ingredients.length
- 1 <= n <= 100
- 1 <= ingredients[i].length, supplies.length <= 100
- 1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
- recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase
  English letters.
- All the values of recipes and supplies combined are unique.
- Each ingredients[i] does not contain any duplicate values.
"""

from collections import defaultdict


class Solution:
    def findAllRecipes(
        self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]
    ) -> list[str]:
        """
        Complexity:
            Time: O(r + i + s)
            Time: O(r + i)
        """
        # create inverse mapping of ingredient to recipe
        ingredients_to_recipes: defaultdict[str, list[str]] = defaultdict(list)
        recipe_missing_count: dict[str, int] = {}
        for recipe, recipe_ingredients in zip(recipes, ingredients):
            recipe_missing_count[recipe] = len(recipe_ingredients)
            for ingredient in recipe_ingredients:
                ingredients_to_recipes[ingredient].append(recipe)

        # iterate through supplies, adding recipes to supplies if all ingredients are present
        res: list[str] = []
        for supply in supplies:
            for recipe in ingredients_to_recipes[supply]:
                recipe_missing_count[recipe] -= 1
                if recipe_missing_count[recipe] == 0:
                    res.append(recipe)
                    supplies.append(recipe)
        return res
