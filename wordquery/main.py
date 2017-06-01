from wordquery.elementIdentifier import *
from wordquery.preprocessor import *
from wordquery.query_generator import *

__author__ = 'ChaminiKD'
# create the knowledgebase
table_list = get_Table_names()
asd = setSementicKB('tables', table_list)

att_list = get_attribute_names()
att = setSementicKB('att', att_list)

s1 = " address of employees "  # w ;
s2 = " What is the  address and  wage  of employees whose  name equal 'John B Smith' "  # w
s3 = " who are the employees"  # w
s4 = " What is the  address and  wage  of employees "  # w
s5 = "wage of employees"  # w
s6 = "address of employees"  # w
s7 = "give me the birthdate of employees"  # w
s8 = "what are the projects?"  # w
s9 = "who are the dependents"  # w
s10 = "what is the name of  employee whose wage equals '25000' "  # w
s11 = "what is the ssn of employee whose sex equals 'M' "  # w
s12 = "what is the birthdate of employee whose name equals 'John B Smith' "  # work
s13 = "what is the name of employee whose wage greaterthan '30000' " #not
s14 = "what are the department names of the departments"
s15 = "what is the name of employee whose wage lessthan '30000'"
s16 = "what is the name of employee whose wage notequal '30000'"

# userInput = input("enter:")
userInput = s16

value, S = getvalue(userInput)
print("value:", value)
print("remaining sentence:", S)

# tokenize the remaining sentence
tokens_of_remaining = getTokenz(S)
print('Tokens of the remaining sentence :', tokens_of_remaining)

# postag_list_of_remaining = pos_tagging(tokens_of_remaining)
# print("Pos tags :", postag_list_of_remaining)

# identify the expression in the user input
# if value:
#     identified_expression = []
#     identified_expression, symbol = identify_expressions(tokens_of_remaining)
#     print("identified expression in the user input =", identified_expression)
# else :
#     value = ''
#     symbol = ''
#     prv_attribute = ''

# identify the condition attribute in the user input
def get_codition_attribute(identified_expression):
    for x in identified_expression:
        exp_index = tokens_of_remaining.index(x)
        print(x, "is in ", exp_index)
        previous_token = []
        previous_token.append(tokens_of_remaining[exp_index - 1])
    return previous_token

# tokenize the user input
tokens = getTokenz(userInput)
print('Tokens:', tokens)

#pos tag the user input
postag_list = []
postag_list = pos_tagging(tokens)
print("Pos tags :", postag_list)

f = open('out/pos_tags.txt', 'w')
for tag in postag_list:
    f.write(str(tag))
    f.write("\n")


# if value:
#     #noun_list  = list(set(postag_list) ^ set(postag_list_of_remaining))
#     new_postag_list  =list(set(postag_list).intersection(postag_list_of_remaining))
# else:
#     new_postag_list = postag_list

noun_list = chunk_nouns(postag_list)
# noun_list.remove(value)
print("Extracted nouns:", noun_list)
print("...........................................................")


# find condition elements
if value:
    identified_expression = []
    identified_expression, symbol = identify_expressions(tokens_of_remaining)
    print("identified expression in the user input =", identified_expression)
    prv_token = []
    prv_token = get_codition_attribute(identified_expression)
    print("previous token =", prv_token)
    prv_attribute = []
    prv_attribute = attributeIdentifier(att, prv_token)
    print("previous attribute = ", prv_attribute)

    # [item for item in postag_list if item == identified_expression]
    # print("++++++++++++++++++++++",postag_list)
    # noun_list = chunk_nouns(postag_list)
    # postag_list.remove(identified_expression)
    # print("newwwwwww:", noun_list)
    # print("...........................................................")

    # remove condition attribute
    list_of_nouns = list(set(noun_list) ^ set(prv_token))
    print("after removing the condition attribute **", list_of_nouns)
    print("..........................................................")
else:
    value = ''
    symbol = ''
    prv_attribute = ''
    list_of_nouns = noun_list


# find tables and attributes in user input
identified_table = []
n_list = []
print("List of nouns..",list_of_nouns)
identified_table, n_list = tableIdentifier(asd, list_of_nouns)
print("Table found:", identified_table)
print("remove this from noun list ******", n_list)

new_nounList = list(set(n_list) ^ set(list_of_nouns))
print("New Noun List, after removing table names", new_nounList)

identified_attribute = []
identified_attribute = attributeIdentifier(att, new_nounList)
print(identified_attribute)
print("Attributes found:", identified_attribute)

# create the sql query
sql = createQuery(identified_attribute, identified_table, value, symbol, prv_attribute)  #################
print(".........................................")
print("Generated SQL  Query : ", sql)

# make database connection
con = makeConnection('root', '', 'company_new')

# get the result
result = getResult(con, sql)
print("Result :", result)
