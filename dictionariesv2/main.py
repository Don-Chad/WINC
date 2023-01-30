# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line


def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    dict = {}
    dict["name"] = name
    dict["date_of_birth"] = date_of_birth
    dict["place_of_birth"] = place_of_birth
    dict["height"] = height
    dict["nationality"] = nationality

    return dict

passport = (create_passport("omari", "01-01-1990", "Amsterdam", 1.80, "The Netherlands"))

# passport= {"John", "01-01-1990", "Amsterdam", 1.80, "Dutch"}

def add_stamp(passport, country):
    if "stamps" not in passport:
        passport["stamps"] = []
    if passport["nationality"] != country and country not in passport["stamps"] :
        passport["stamps"].append(country)
    return passport
    
    
# add_stamp(passport, "The Netherlands")
# add_stamp(passport, "The Netherlands")
# add_stamp(passport, "Volendam")
# add_stamp(passport, "Volendam")
# add_stamp(passport, "Volendam")



def add_biometric_data(passport, biometric_data_type, new_data, biometric_date):
    if "biometric" not in passport:
        passport["biometric"] = {}
    if biometric_data_type not in passport["biometric"]: 
        passport["biometric"][biometric_data_type] = {} 
    biometric_input = {}
    biometric_input["date"] = biometric_date
    biometric_input["value"] = new_data
    passport["biometric"][biometric_data_type] = biometric_input
    return passport

    
omari = create_passport("Omari Muchumba", "1995-07-16", "Kampala", 184.31, "Uganda")
add_biometric_data(omari, "eye_color_left", "blue", "2020-05-05")
add_biometric_data(omari, "eye_color_right", "green", "2020-05-05")

fingerprint_data = {
    "left_pinky": "2378945",
    "left_ring": "2349081",
    "left_middle": "132890",
    "left_index": "9823234",
    "left_thumb": "0924131",
    "right_thumb": "6234923",
    "right_index": "13249734",
    "right_middle": "34023784",
    "right_ring": "12332538",
    "right_pinky": "32458970",
}

omari = add_biometric_data(omari, "finger_prints", fingerprint_data, "2022-01-12")
print(omari)

print(omari)



import json
print(json.dumps(omari, indent=4))



# The biometric data should live in a dictionary inside of the passport. 
# In other words: a nested dictionary. The key for the biometric data dictionary is biometric.

# The function should return:

# If the passport did not yet have any biometric data: add the key for it,
#  you can assume you'll only get passports with a chip to save biometric data.

# If the type of biometric data was not yet in the passport: add it to the passport.
# The value for the specific type of biometric data should again be a dictionary (so nested again). 

# This dictionary should have two keys: date and value. See examples below for specific examples.
# If the type of biometric data was already in the passport: update the biometric data in the passport, overwriting the previous value and date.




