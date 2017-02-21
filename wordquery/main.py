from wordquery.elementIdentifier import *
from wordquery.preprocessor import *
from wordquery.query_generator import *

__author__ = 'ChaminiKD'

# userInput = " What is the birthdate and address of employee 'John B Smith' "
userInput = " What is the  address and  wage  of employee 'John B Smith' "

value, S = getvalue(userInput)
print("value:", value)
# print("remaining sentence", S)

tokens = getTokenz(userInput)
print('Tokens:',tokens)

postag_list = []
postag_list = pos_tagging(tokens)
print("Pos tags :", postag_list)

f = open('out/pos_tags.txt', 'w')
for tag in postag_list:
    f.write(str(tag))
    f.write("\n")

noun_list = chunk_nouns(postag_list)
print("Extracted nouns:",noun_list)
print(".........................................")

tables = extract_tables(noun_list)
attributes = extract_attributes(noun_list)

table_list = get_Table_names()
asd = setSementicKB('tables', table_list)

identified_table = []
identified_table = tableIdentifier(asd, noun_list)
print("Table found:", identified_table)

att_list = get_attribute_names()
att = setSementicKB('att', att_list)

identified_attribute = []
identified_attribute = attributeIdentifier(att, noun_list)
print("Attributes found:", identified_attribute)

sql = createQuery(identified_attribute, identified_table)
print(".........................................")
print("Generated SQL  Query : ", sql)

con = makeConnection('root', '', 'company')

result = getResult(con, sql)
print("Result :", result)
