MEALS_LIST_PATH = "./Results/meal_list.tsv"
DISTINC_MEALS_PATH = "./Results/distinct_meal_list.tsv"

file = open(MEALS_LIST_PATH)
write_file = open(DISTINC_MEALS_PATH, "w")

different_meals = set([])
for line in file.readlines():
    just_meals = line.split("\t")[0]

    different_meals.add(just_meals)

for item in different_meals:
    write_file.write("\t".join(item.split(","))+"\n")