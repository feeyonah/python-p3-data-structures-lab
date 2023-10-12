spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food["name"]for food in spicy_foods]
    return names 

def get_spiciest_foods(spicy_foods):
    spiciness=[spice for spice  in spicy_foods if spice["heat_level"] >5]
    return spiciness

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spice in spicy_foods:
        if spice['cuisine']==cuisine:
            return spice
            #An example of how to use tiis function
results=get_spicy_food_by_cuisine( spicy_foods,"American")
print(results)
def print_spiciest_foods(spicy_foods):
    hot_and_sweet = get_spiciest_foods(spicy_foods)
    for spice in hot_and_sweet:
        heat_level = "🌶" * spice["heat_level"]
        print(f"{spice['name']} ({spice['cuisine']}) | Heat Level: {heat_level}")

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0
    addition=sum(food["heat_level"] for food in spicy_foods)
    average=addition//len(spicy_foods)
    return average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
#an example of how to use this function
spicy_food={
"name":"maize",
"cuisan":"portugal",
"heat_level":"4"

}
new_spicy_foods=create_spicy_food(spicy_foods,spicy_food)
print(new_spicy_foods)