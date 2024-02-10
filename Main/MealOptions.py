
RESULT_PATH = "./Results/meal_list.tsv"
JSON_RESULT_PATH = "./Results/meal_list.json"
import json

def convert_hash_to_list(hash):
    list = []

    for key in hash:
        list.append(hash[key])

    return list

official_meal_list = []

def meal_backtracker(health_bounds, meals, index, day_worth_of_meals_list, day_meal_categories):
    global official_meal_list

    if index == len(meals):
        return

    day_meal_categories.append(meals[index].name)
    for meal in meals[index].meals:
        day_worth_of_meals_list.append(meal)

        if health_bounds.is_within_bounds(day_worth_of_meals_list):
            official_meal_list.append((list(day_worth_of_meals_list), list(day_meal_categories)))

        if not health_bounds.is_over_bounds(day_worth_of_meals_list):
            meal_backtracker(health_bounds, meals, index+1, day_worth_of_meals_list, day_meal_categories)

        day_worth_of_meals_list.pop()
    day_meal_categories.pop()

    meal_backtracker(health_bounds, meals, index+1, day_worth_of_meals_list, day_meal_categories)

def write_meal_options():
    global official_meal_list

    file = open(RESULT_PATH, "w")

    for entry, meal_category in official_meal_list:

        string = ",".join(meal_category) + "\t\t"

        for entr in entry:
            string += ",".join(entr.name) +","

        file.write(string + "\n")

def write_meal_options_json():
    global official_meal_list
    meal_options = {}



    count = 1
    for entry, meal_category in official_meal_list:
        key = "meal"+str(count)
        count +=1

        meal_options[key] = {}

        for i in range(len(entry)):
            meal = meal_category[i]
            entr = entry[i]

            meal_options[key][meal] = entr.name

    json_object = json.dumps(meal_options)

    with open(JSON_RESULT_PATH, "w") as outfile:
        outfile.write(json_object)

def get_meal_options(meals, health_bounds):
    global official_meal_list

    meal_list = convert_hash_to_list(meals)

    meal_backtracker(health_bounds, meal_list, 0, [], [])

    write_meal_options_json()
