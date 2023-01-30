# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line

# import this
import time



def wait(seconds):
    begin = time.time()
    
    end = time.time()
    progres = end - begin
    while progres < seconds:
        end = time.time()
        progres = end - begin

    
# wait(1)

import math

def mysun(number):
    sin = math.sin(number)
    return sin


print(mysun(4))

from datetime import datetime

# get current datetime

today = datetime.now()
print('Today Datetime:', today)

iso_date = today.isoformat()
print(iso_date)


import sys
def platform():
    platform = sys.platform
    return platform

print(platform())

from greet import supergreeting

print (supergreeting("bob"))



def supergreeting_wrapper(name):
    return supergreeting(name)
     
    

print(supergreeting("bob"))