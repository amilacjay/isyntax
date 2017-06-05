from nltk.corpus import stopwords

__author__ = 'ChaminiKD'

content = [('What', 'WP'), ('is', 'VBZ'), ('the', 'DT'), ('address', 'NN'), ('and', 'CC'), ('wage', 'NN'), ('of', 'IN'), ('employees', 'NNS'), ('whose', 'WP$'), ('name', 'NN'), ('equal', 'JJ'), ("'John", 'NN'), ('B', 'NNP'), ('Smith', 'NNP'), ("'", 'POS')]
value = 'John B Smith'
valueList = []
valueList = value.split(" ")
print(valueList)
contentnew = []

escapeWords = ['what', 'who', 'whose', 'display', 'is', 'a', 'at', 'is', '.', ',', '(', ')', 'equal', 'equals']
# remove escape words
def remove_stopWords(content):
    print(content)
    for x in content:
        filtered_words = [word for word in x if word not in stopwords.words('english')]
        resultWords = [word for word in filtered_words if word.lower() not in escapeWords]
        if len(resultWords)>1:
            contentnew.append(resultWords)
    return contentnew



def filter_pos(content, vlist):
    ilist = []
    for x in vlist:
        index = 0
        for y in content:
            #print('*****',x,y[0])
            if x.lower() == str(y[0]).lower():
                print("***")
                ilist.append(index)
            index=index+1

    for a in ilist:
        print(a)

token = "what is the birthdate of employee whose name equals 'John B Smith'"

def add_space(token):
    # index = token.find("'")
    # if index != -1:
    #    if token[index+1] != ' ':
    #       token = (token[:index+1]+' '+token[index+1:])
    #       print(token)

    ilist = []
    index = 0
    while index < len(token):
        index = token.find("'", index)
        if index == -1:
            break
        ilist.append(index)
        print(token)
        index += 1
    for x in ilist:
        token = (token[:x+1]+' '+token[x+1:])
    print(token)

v = remove_stopWords(content)
print(v)
#filter_pos(content, valueList)
#add_space(token)