# Objectives : Build interactive meaning finder of words
#Author : Abdul Joheb Ansari

import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def findmeaning(words):
    words = words.lower()                   #Changes entered worde to lower since most of the words in json file is in lower case
    if words in data:                       # Allows to extecute entry in CHarM, COOk
        return data[words]
    elif words.title() in data:             # Allows search for Proper Noun like Delhi, New york
        return data[words.title()]
    elif words.upper() in data:             # Allows search for all upper case words like NATO USA
        return data[words.upper()]
    elif len(get_close_matches(words, data.keys()))>0:
        yesno = input("Did you mean %s instead? Enter Y if Yes, or N for No :" % get_close_matches(words,data.keys())[0])
        if yesno == "Y":
            return data[get_close_matches(words, data.keys())[0]]
        elif yesno == "N":
            return "Check Spelling" 
        else:
            return "The system does not understand your input"
    else:
        return "The word was not found. Please check spelling"


here = input("Enter your word:")

output = findmeaning(here)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

