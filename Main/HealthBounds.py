class HealthBounds:
    def __init__(self, calorie, fat, carb, protein, max_sugar):
        self.bounds = {
            "cal": [calorie - 25, calorie + 25],
            "fat": [fat - 10, fat + 10 ],
            "carb": [carb - 10, carb + 10],
            "protein": [protein - 10, protein + 10],
            "sugar":[0,max_sugar]
        }

    def is_within_bounds(self, meal_list):
        return not self.is_under_bounds(meal_list) and not self.is_over_bounds(meal_list)

    def get_meal_result(self, meal_list):
        result = meal_list[0]

        for meal in meal_list[1:]:
            result += meal

        return result

    def is_under_bounds(self, meal_list):
        result = self.get_meal_result(meal_list)

        for value_name, value_actual in [("cal", result.cal), ("fat", result.fat), ("carb", result.carb), ("protein", result.protein), ("sugar", result.sugar)]:
            if value_actual < self.bounds[value_name][0]:
                return True
        return False

    def is_over_bounds(self, meal_list):
        result = self.get_meal_result(meal_list)

        for value_name, value_actual in [("cal", result.cal), ("fat", result.fat), ("carb", result.carb), ("protein", result.protein), ("sugar", result.sugar)]:
            if value_actual > self.bounds[value_name][1]:
                return True
        return False
