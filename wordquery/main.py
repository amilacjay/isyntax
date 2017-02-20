from wordquery.elementIdentifier import *
from wordquery.preprocessor import *

__author__ = 'ChaminiKD'

userInput = " What is the birthdate and address of employee 'John B Smith' "

value, S = getvalue(userInput)
print("value", value)
print("remaining sentence", S)

tokens = getTokenz(userInput)
print(tokens)

postag_list = []
postag_list = pos_tagging(tokens)
print("pos tags", postag_list)

f = open('out/pos_tags', 'w')
for tag in postag_list:
    f.write(str(tag))
    f.write("\n")

noun_list = chunk_nouns(postag_list)
print(noun_list)

tables = identify_tables(noun_list)
attributes = identify_attributes(noun_list)











