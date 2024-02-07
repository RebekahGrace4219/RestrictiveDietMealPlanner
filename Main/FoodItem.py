from multiset import *

CALORIE_PATH = "Data\Calories.tsv"
class FoodItem:
    def __init__(self, name, cal, fat, carb, protein, sugar):
        self.name = name
        self.cal = float(cal)
        self.fat = float(fat)
        self.carb = float(carb)
        self.protein = float(protein)
        self.sugar = float(sugar)

    def __add__(self, other):
        name = self.name + other.name
        cal = self.cal + other.cal
        fat = self.fat + other.fat
        carb = self.carb + other.carb
        protein = self.protein + other.protein
        sugar = self.sugar + other.sugar
        return FoodItem(name, cal, fat, carb, protein, sugar)

    def __str__(self):
        return "\t".join([",".join(self.name)+"\n", str(self.cal), str(self.fat), str(self.carb), str(self.protein), str(self.sugar)])

    def __eql__(self, other):
        return Multiset(other.name) == Multiset(self.name)

def get_base_food_items():
    base_food_items = {}

    for line in open(CALORIE_PATH).readlines()[1:]:
        items = line.replace("\n", "").split("\t")

        if items[0] == "":
            continue
        cal = FoodItem([items[0]], items[1], items[2], items[3], items[4], items[5])

        base_food_items[items[0]] = cal
    return base_food_items