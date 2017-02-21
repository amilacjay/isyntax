from wordquery.elementIdentifier import *
from wordquery.preprocessor import *
from wordquery.query_generator import *

__author__ = 'ChaminiKD'

# userInput = " What is the birthdate and address of employee 'John B Smith' "
userInput = " What is the  address of employee 'John B Smith' "

value, S = getvalue(userInput)
print("value", value)
print("remaining sentence", S)

tokens = getTokenz(userInput)
print(tokens)

postag_list = []
postag_list = pos_tagging(tokens)
print("pos tags", postag_list)

f = open('out/pos_tags.txt', 'w')
for tag in postag_list:
    f.write(str(tag))
    f.write("\n")

noun_list = chunk_nouns(postag_list)
print(noun_list)

tables = extract_tables(noun_list)
attributes = extract_attributes(noun_list)

table_list = get_Table_names()
asd = setSementicKB('tables', table_list)
identified_table = []
identified_table = tableIdentifier(asd, noun_list)
print("the found table is", identified_table)

sql = createQuery("", identified_table)

con = makeConnection('root', '', 'company')

result = getResult(con, sql)
print(result)
