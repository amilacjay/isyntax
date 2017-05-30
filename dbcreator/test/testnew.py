from nltk import *

text = "students' name is nimal"
w = word_tokenize(text)
p = pos_tag(w)

print(p)