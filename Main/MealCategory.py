MEAL_PATH = "Data\Meals.tsv"

class MealCategory:
    def __init__(self, name):
        self.name = name
        self.meals = []

    def add_meal(self, item_list, base_food_items):
        result = base_food_items[item_list[0]]

        for i in range(1, len(item_list)):
            result += base_food_items[item_list[i]]

        self.meals.append(result)

    def __str__(self):
        string = "Meal: "+self.name +"\n"

        for meal in self.meals:
            string += "\t"+str(meal)+"\n"

        return string

    def __eq__(self, other):
        return self.name == other.name

def get_meals(base_food_items):
    mealCategories = {}

    for line in open(MEAL_PATH):
        line = line.replace("\n", "")
        items = line.split("\t")

        mealName = items[0]

        if mealName == "":
            continue

        mealCategories[mealName] = mealCategories.get(mealName, MealCategory(mealName))

        mealCategories[mealName].add_meal(items[1:], base_food_items)

    return mealCategories