import re
from wordquery.preprocessor import *

__author__ = 'ChaminiKD'

# S = input("Enter: ")
# What is the birthdate and address of employee 'John B Smith'

S = " What is the birthdate and address of employee 'John B Smith' "

# Getting the value from the text
def getvalue(S):
    pattern = re.compile('\'[A-Za-z0-9 _-]*\'', re.IGNORECASE)
    listofHits = re.findall(pattern, S)
    if listofHits:
        for hitWord in listofHits:
            # values = hitWord
            S = S.replace(hitWord, " ", 1)
            print('Values =', hitWord)
    else:
        print("No value provided by the user")
    getTokenz(S)


getvalue(S)














