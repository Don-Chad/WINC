# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

def alphabetical_order(list_of_filmnames):
    sorted_list = sorted(list_of_filmnames) 
    pass


golden_globe_film_list = ["Close Encounters of the Third Kind", "E.T. the Extra-Terrestrial", "The Color Purple", "Schindler's List"]

def won_golden_globe(filmname):
    if filmname.lower() in [title.lower() for title in golden_globe_film_list]:
        return True
    else:
        return False

print(won_golden_globe("Close Encounters of the Third Kind"))


list_of_all_toto_albums =["Fahrenheit","The Seventh One", "Toto XX","Falling in Between", "Toto XIV", "Old Is New"]

def remove_all_toto_albums(work_of_son):
    
    updated_list = []
    for album in work_of_son:
        if album not in list_of_all_toto_albums:
            updated_list.append(album)
    
    return updated_list

print (remove_all_toto_albums(["Fahrenheit","yet another album to check"]))