import pandas as pd
from multiset import *
from FoodItem import get_base_food_items
from MealCategory import get_meals
from MealOptions import get_meal_options
from HealthBounds import HealthBounds

# TODO ADD
# mini bao buns
# half cup white rice

### TODO: name meals and their options so it doesnt try to make the same meals within the same day


base_food_items = get_base_food_items()
meals = get_meals(base_food_items)
RebekahHealthBounds = HealthBounds(1175, 45, 155, 55, 50)

mealOptions = get_meal_options(meals, RebekahHealthBounds)
