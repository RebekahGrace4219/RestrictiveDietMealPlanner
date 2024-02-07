
RESULT_PATH = "./Results/meal_list.tsv"
def convert_hash_to_list(hash):
    list = []

    for key in hash:
        list.append(hash[key])

    return list

official_meal_list = []
end_counter = 0
maximum_endings = 1

def meal_backtracker(health_bounds, meals, index, day_worth_of_meals_list, day_meal_categories):
    global official_meal_list
    global end_counter

    if index == len(meals):
        end_counter += 1
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

def get_meal_options(meals, health_bounds):
    global official_meal_list
    global maximum_endings

    meal_list = convert_hash_to_list(meals)

    for meal in meal_list:
        maximum_endings *= len(meal.meals)


    meal_backtracker(health_bounds, meal_list, 0, [], [])

    write_meal_options()
