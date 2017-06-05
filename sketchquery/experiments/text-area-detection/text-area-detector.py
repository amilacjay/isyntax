import cv2
import numpy as np
from sketchquery.core import *
from sketchquery.model import *

image = cv2.imread('../../samples/sketches/sketch_typed_separated.jpg', cv2.IMREAD_COLOR)

ratio, resized = optimalSize(image, sqr=800)
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
thresh = binaryImage(gray)

textPartsWithStats = textRegionsWithStats(thresh)

for i in range(len(textPartsWithStats)):
    textPart = textPartsWithStats[i][0]
    stat = textPartsWithStats[i][1]
    cv2.rectangle(resized, (stat[0],stat[1]), (stat[0]+stat[2], stat[1]+stat[3]), (0, 255, 0), 2)
    print(imageToText(textPart))
    # cv2.imshow('T'+str(i), textPart)


cv2.imshow('resized', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()


