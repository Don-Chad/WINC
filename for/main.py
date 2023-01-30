from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """



def shortlist(countries):
    shortest = "aadsdaveryaverylongvalue"
    
    short_list = ''
    for value in countries:
        if len(value) < len(shortest):
            shortest = value
            short_list = value
        if len(value) == len(shortest):
            short_list = shortest + " " + value
    return short_list


def most_vowels(countries):
    vowel_number = []

    for value in countries:
        count = 0

        for character in value:
            if character in 'aeiou':
                count = count + 1

        vowel_number.append([count, value])

    vowel_number.sort(reverse=True)

    top_three = []

    for count, value in vowel_number:
        if len(top_three) < 3:
            top_three.append(value)

    return top_three



def alphabet_set(countries):
  alphabet = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
  result = []
  for i in range(1, len(countries)+1):
    combinations = make_combinations(countries, i)
    for combination in combinations:
      letters = set()
      for country in combination:
        for letter in country:
          letters.add(letter.upper())
      if letters == alphabet:
        result.append(combination)
  if result:
    return min(result, key=len)
  else:
    return result

def make_combinations(items, n):
  if n==0:
    return [[]]
  combinations = []
  for i in range(len(items)):
    for c in make_combinations(items[i+1:], n-1):
      combinations.append([items[i]] + c)
  return combinations











# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """



print(shortlist(countries))
print(most_vowels(countries))

