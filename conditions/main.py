# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

def farm_action(weather, time_of_day, cow_milking_status, location_of_cows, season, slurry_tank, grass_status):
    actions = ""
    action_number = 0
    
    if (location_of_cows == "pasture" and time_of_day == "night") or weather == "rainy":
        actions = actions + ("take cows to cowshed")
        location_of_cows = "cowshed"
    
    if cow_milking_status and location_of_cows == "cowshed":
        actions = actions + ("*milk cows")
    
    if (slurry_tank and location_of_cows == "cowshed" and weather not in ["sunny", "windy"]):
        actions = actions +("*fertilize pasture")
    
    if grass_status and season == "spring" and weather == "sunny" and location_of_cows != "pasture":
        actions = actions + ("*mow grass")
    
    if not actions:
        actions = actions + ("*wait")
    
    if location_of_cows == "cowshed" and actions[-1] in ["milk cows", "fertilize pasture", "mow grass"]:
        actions = actions + ("*take cows back to pasture")
    if actions == "":
        Print("no actions")
    else:
        print(actions)

s = actions

count = 0
output = ''
start_pos = s.find('*')
while start_pos != -1:
    count += 1
    output += s[:start_pos]
    s = s[start_pos+1:]
    start_pos = s.find('*')
output += s
if count >= 2:
    output = output + '\n' * (count - 1)


input_string = "This is a *test* string *with* stars"
output_string, star_count = remove_and_count_stars(input_string)
print("Output String:", output_string)
print("Star Count:", star_count)



farm_action("rainy", "night", True, "cowshed", "winter", True, True)
 