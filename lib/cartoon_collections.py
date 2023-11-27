def roll_call_dwarves(dwarves):
    for index, dwarf in enumerate(dwarves, start=1):
        print(f"{index}. {dwarf}")

def summon_captain_planet(calls):
    return [f"{call.capitalize()}" + '!' for call in calls]

def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)

def find_the_cheese(foods):
    cheeses = ["cheddar", "gouda", "camembert"]

    for food in foods:
        if food in cheeses:
            return food
    return None
