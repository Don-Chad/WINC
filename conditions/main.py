# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action(weather, time_of_day, cow_milking_status, location_of_cows, season, slurry_tank, grass_status):
    actions = "wait"
    before_action = "take cows to cowshed\n"
    action_after = "take cows back to pasture"

    
    if cow_milking_status == True and location_of_cows == "pasture":
        actions = before_action
        


    if weather == "rainhy" or (location_of_cows == "pasture" and time_of_day == "night"):
        actions = ""
        print(actions)
        return actions

    
    
    if cow_milking_status == True and location_of_cows == "cowshed":
        actions = ("milk cows")
        print("milk cows")
        return actions

    if slurry_tank == True and location_of_cows == "pasture" and weather not in ["sunny", "windy"]:
        actions = ("take cows to cowshed\n" + "fertilize pasture\n" + "take cows back to pasture")
        print(actions)
        return actions

    if slurry_tank == True and location_of_cows == "cowshed" and weather not in ["sunny", "windy"]:
        actions = "fertilize pasture"
        print(actions)
        return actions

    if grass_status == True and season == "spring" and weather == "sunny" and location_of_cows == "pasture":
        actions = "take cows to cowshed\n" + "mow grass\n" + "take cows back to pasture" 
        print(actions)
        return actions

    if grass_status == True and season == "spring" and weather == "sunny" and location_of_cows != "pasture":
        actions = ("mow grass")
        print(actions)
        return actions

    else:
        actions = ("wait")
        print(actions)
        return actions

print(farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))


