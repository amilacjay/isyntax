from nltk.metrics import *


def withMinEditDist(word, list):
    if len(list) >0:
        suitableWord = list[0]

        for item in list:
            if edit_distance(word, suitableWord) > edit_distance(word, item):
                suitableWord = item
        return suitableWord
    else:
        return word



print(withMinEditDist('r00m', ['room', 'booking', 'hotel', 'customer']))


