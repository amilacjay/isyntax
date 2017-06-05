from wordquery.elementIdentifier import *
from wordquery.preprocessor import *
from wordquery.query_generator import *
from operator import sub

__author__ = 'ChaminiKD'
xml_file = 'company_new.xml'
# create the knowledgebase
table_list = get_Table_names(xml_file)
asd = setSementicKB('tables', table_list)

att_list = get_attribute_names(xml_file)
att = setSementicKB('att', att_list)

s1 = " address of employees "  # w ;
s2 = " What is the  address and  wage  of employees whose  name equal 'John B Smith'"  # w
s3 = " who are the employees"  # w
s4 = " What is the  address and  wage  of employees "  # w
s5 = "wage of employees"  # w
s6 = "address of employees"  # w
s7 = "give me the birthdates of employees"  # w
s8 = "what are the projects?"  # w
s9 = "who are the dependents"  # w
s10 = "what is the name of  employee whose wage equals '25000' "  # w
s11 = "what is the ssn of employee whose sex equals 'M' "  # icorrect
s12 = "what is the birthdate of employee whose name equals 'John B Smith' "  # not work
s13 = "what is the name of employee whose wage greaterthan '30000' "  # w
s14 = "what are the departmentnames of the departments" #w
s15 = "what is the name of employee whose wage lessthan '30000'" #w
s16 = "what is the name of employee whose wage notequal '30000'" #w
s17 = "what is the name of employee whose wage equals '30000' and departmentnumber equals '5' "  # w
s18 = "what is the name of employee whose sex equals 'M' or departmentnumber equals '5' "  # w
s19 = "what is the supervisorssn of employee whose wage notequal '30000'"  # w
s20 = "what is the sex of employee whose wage lessthan '30000'"

# userInput = input("enter:")
userInput = s2
Input = add_space(userInput)
print("Input :", Input)

value, S = getvalue(Input)
print("value:", value)
print("remaining sentence", S)

if value:
    for v in value:
        v = v[:1] + v[2:]
else:
    value = ''

# tokenize the remaining sentence
tokens_of_remaining = getTokenz(S)
print("tokens_of_remaining", tokens_of_remaining)

# identify the condition attribute in the user input
def get_codition_attribute(i):
    # for x in identified_expression:
    # exp_index = tokens_of_remaining.index(x)
    exp_index = i[1]
    # print(x, "is in ", exp_index)
    previous_token = []
    previous_token.append([tokens_of_remaining[exp_index - 1], i[0]])
    return previous_token

# tokenize the user input
tokens = getTokenz(Input)

# pos tag the user input
postag_list = []
postag_list = pos_tagging(tokens)
print("Pos tags :", postag_list)

f = open('out/pos_tags.txt', 'w')
for tag in postag_list:
    f.write(str(tag))
    f.write("\n")

postag_list = remove_escapeWords(postag_list)
print("****After removing escape words :", postag_list)
noun_list = chunk_nouns(postag_list)
# print("After chunking : ", noun_list)
# noun_list = noun_list[0].split(' ')
print("Extracted nouns by cunking :", noun_list)
print("...........................................................")

# find condition elements
if value:
    identified_expression = []
    symbol = []
    identified_expression, symbol = identify_expressions(tokens_of_remaining)
    print("identified expression in the user input =", identified_expression)
    print("identified symbols in the user input =", symbol)
    condition_att_list = []
    privious_token_list = []
    for i in identified_expression:
        prv_token = []
        prv_token = get_codition_attribute(i)
        print("previous token =", prv_token)
        privious_token_list.append(prv_token[0][0])
        prv_attribute = []
        prv_attribute = attributeIdentifier(att, prv_token[0])
        print("previous attribute = ", prv_attribute)
        condition_att_list.append([prv_attribute[0], i[2]])

    print("condition attribute list", condition_att_list)
    # print("GGGGGGGGGGGGGGg",privious_token_list)

    # remove condition attribute
    list_of_nouns = [word for word in noun_list if word.lower() not in privious_token_list]
    print("after removing the condition attributes **", list_of_nouns)

    operator = find_operators(userInput)
    print("operators found :", operator)
    if operator:
        operator = operator
    else:
        operator = ''
    print("..........................................................")

else:
    value = ''
    symbol = ''
    prv_attribute = ''
    list_of_nouns = noun_list
    operator = ''
    condition_att_list = ''


# find tables and attributes in user input
identified_table = []
n_list = []
print("*****List of nouns          :", list_of_nouns)
identified_table, n_list = tableIdentifier(asd, list_of_nouns)
print("*****Table found            :", identified_table)
# print("*****remove this table name from noun list :", n_list)

new_nounList = list(set(n_list) ^ set(list_of_nouns))
print("*****New Noun List, after removing table names : ", new_nounList)

identified_attribute = []
identified_attribute = attributeIdentifier(att, new_nounList)
# print(identified_attribute)
print("*****Attributes found       :", identified_attribute)

# if len(condition_att_list) < 2:
#     condition_att_list = ''

print("*****value                  :", value)
print("*****symbol                 :", symbol)
print("*****prv attribute          :", prv_attribute)
print("*****conditon atribute list :", condition_att_list)

# create the sql query
sql = createQuery(identified_attribute, identified_table, value, symbol, prv_attribute, condition_att_list, operator)
print(".........................................")
print("Generated SQL  Query : ", sql)

# make database connection
con = makeConnection('root', '', 'company_new')

# get the result
result = getResult(con, sql)
print("Result :", result)
