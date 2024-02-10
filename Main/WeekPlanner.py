from FoodItem import get_base_food_items, FoodItem

JSON_PATH = "./Results/meal_list.json"

def read_file():
    global JSON_PATH

    import json
    with open(JSON_PATH, 'r') as openfile:
        return json.load(openfile)


meal_file = read_file()
meal_list = ["85", "87", "88", "138", "139", "141", "142"]

def get_meals_usage():
    global meal_file
    global meal_list

    hash_count = {}

    for meal in meal_list:
        key = "meal" + meal

        item = meal_file[key]

        for entry in item:
            value = item[entry]
            for i in value:
                hash_count[i] = hash_count.get(i, 0) + 1

    for key in hash_count:
        print(hash_count[key], key)

def get_meal_criteria():
    global meal_file
    global meal_list

    banned_list = set(["Bagel", "Cheerios", "Quesadilla"])
    looking_list = set(["Peanut Butter Sandwhich"])

    for mealKey in meal_file.keys():
        item = set(meal_file[mealKey].keys())

        if mealKey[4:] in meal_list:
            continue
        if len(item.intersection(banned_list)) > 0:
            continue
        if len(item.intersection(looking_list)) > 0:
            print(mealKey)
            break

def print_day_usage(days):
    for i in range(len(days)):
        result = days[i]
        print(i+1, result.cal, result.fat, result.carb, result.protein, result.sugar)

def get_days_usage():
    global meal_file
    global meal_list

    base_food_items = get_base_food_items()
    macro_results = []

    for key in meal_list:
        result = FoodItem([""], 0, 0, 0, 0, 0)
        mealKey = "meal" + key

        meal_categories = meal_file[mealKey]

        for meal_category in meal_categories:
            for item in meal_categories[meal_category]:
                result += base_food_items[item]

        macro_results.append(result)

    print_day_usage(macro_results)

def print_meals():
    global meal_file
    global meal_list

    for key in meal_list:
        mealKey = "meal" + key

        meal  = meal_file[mealKey]

        for key in meal:
            print(meal[key])
        print("")
print_meals()