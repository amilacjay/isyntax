import re


text = "NNP"

regex = re.compile('NN.*')

matchObj = regex.match(text)

if(matchObj is not None):
    print(matchObj.span())
else:
    print(matchObj)