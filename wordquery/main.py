from wordquery.elementIdentifier import *
from wordquery.preprocessor import *
from wordquery.query_generator import *
from operator import sub
from wordquery.table_fetcher import *

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
s14 = "what are the departmentnames of the departments"  # w
s15 = "what is the name of employee whose wage lessthan '30000'"  # w
s16 = "what is the name of employee whose wage notequal '30000'"  # w
s17 = "what is the name of employee whose wage equals '30000' and departmentnumber equals '5' "  # w
s18 = "what is the name of employee whose sex equals 'M' or departmentnumber equals '5' "  # w
s19 = "what is the supervisorssn of employee whose wage notequal '30000'"  # w
s20 = "what is the sex of employee whose wage lessthan '30000'"  # not
s21 = 'ssn of employees'
s22 = " employee name whose departmentname equals 'headquarters' "
s23 = " employee details whose departmentname equals 'headquarters' "

# userInput = input("enter:")
userInput = s23
Input = add_space(userInput)  # add space
print("Input :", Input)

value, S = getvalue(Input)
print("value:", value)
print("remaining sentence", S)

if value:
    v_list = []
    for v in value:
        v = v[:1] + v[2:]  # remove space
        v_list.append(v)
    print(v_list)
    value = v_list
else:
    value = ''

# tokenize the remaining sentence
tokens_of_remaining = getTokenz(S)
print("tokens_of_remaining", tokens_of_remaining)

# tokenize the user input
tokens = getTokenz(Input)

# pos tag the user input
postag_list = pos_tagging(tokens)
print("Pos tags :", postag_list)

f = open('out/pos_tags.txt', 'w')
for tag in postag_list:
    f.write(str(tag))
    f.write("\n")

postag_list = remove_escapeWords(postag_list)
print("****After removing escape words :", postag_list)
noun_list = chunk_nouns(postag_list)
print("Extracted nouns by cunking :", noun_list)
print("...........................................................")


# find condition elements
if value:
    symbol, prv_attribute, list_of_nouns, operator, condition_att_list = find_condition_elements(tokens_of_remaining,
                                                                                                 att, noun_list,
                                                                                                 userInput, xml_file)
else:
    value = ''
    symbol = ''
    prv_attribute = ''
    list_of_nouns = noun_list
    operator = ''
    condition_att_list = ''


# find tables and attributes in user input
print("*****List of nouns          :", list_of_nouns)
identified_table, n_list = tableIdentifier(asd, list_of_nouns, xml_file)
identified_table = list(identified_table)
print("*****Table found            :", identified_table)

new_nounList = list(set(n_list) ^ set(list_of_nouns))
print("*****New Noun List, after removing table names : ", new_nounList)

identified_attribute = attributeIdentifier(att, new_nounList, xml_file)
print("*****Attributes found       :", identified_attribute)
print("*****value                  :", value)
print("*****symbol list            :", symbol)
print("*****prv attribute          :", prv_attribute)
print("*****conditon atribute list :", condition_att_list)

tab_att_list = table_extractor()
print("tables with corresponding attributes", tab_att_list)
sql = ""
for t in tab_att_list:
    if t[0][0] == identified_table[0]:
        at_set = t[1]
        print("ttttt", at_set)

        if condition_att_list == '' or condition_att_list[0][0] in at_set:

            print("yesss")
            sql = createQuery(identified_attribute, identified_table, value, symbol, prv_attribute, condition_att_list,
                              operator)
        else:
            print("noooo")
            reference_list = get_referenceTable(identified_table, condition_att_list)
            print("reference tables:", reference_list)
            print("***",prv_attribute)
            list_table = table_extractor()
            print("listt", list_table)

            index_selected = check_reftable(list_table, reference_list, prv_attribute)
            print("index selcted:" , index_selected)
            ref_tables = (list_table[index_selected])[0]
            print("ref tables" , ref_tables)
            sql = create_twoTable_query(ref_tables[0], identified_table[0], list_ref, identified_attribute, value,
                                        prv_attribute)



# create the sql query
# sql = createQuery(identified_attribute, identified_table, value, symbol, prv_attribute, condition_att_list, operator)
print(".........................................")
print("Generated SQL  Query : ", sql)

# make database connection
con = makeConnection('root', '', 'company_new')

# get the result
result = getResult(con, sql)
print("Result :", result)
