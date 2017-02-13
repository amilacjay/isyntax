import cv2
import numpy as np
from sketchquery.core import *
from sketchquery.model import *


image = cv2.imread('../samples/sketches/sketch_typed_opened_1.jpg', cv2.IMREAD_COLOR)

ratio, resized = optimalSize(image, sqr=550)

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

thresh = binaryImage(gray)
removed = thresh.copy()

textPartsWithStats = textRegionsWithStats(thresh)

table = Table()
uncategorized = []

for i in range(len(textPartsWithStats)):
    textPart = textPartsWithStats[i][0]
    stat = textPartsWithStats[i][1]
    text = imageToText(textPart).strip()
    cv2.imshow(str(i), textPart)

    removed[stat[1]:stat[1] + stat[3], stat[0]:stat[0] + stat[2]] = 0

    ret, conts, hier = cv2.findContours(removed.copy(), mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

    isEnclosedByCircle, hull = enclosedByCircle(stat, conts)

    if text.startswith('[') and text.endswith(']'):
        projectionFields = text.replace('[','').replace(']','').replace(' ','').split(',')
        table.setProjectionFields(projectionFields)

    elif '=' in text:
        table.setCondition(text)

    elif isEnclosedByCircle:
        table.name = text

    else:
        uncategorized.append(textPart)


# ret, conts, hier = cv2.findContours(removed, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
# approx = [cv2.approxPolyDP(c, 3, True) for c in conts]

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 20,param1=50,param2=30, minRadius=10)
# print(circles)
test = np.ones((removed.shape[0], removed.shape[1],3))*255

for cir in circles[0]:
    x, y, r = cir
    cv2.circle(test, (x, y), r, (0, 255, 0), 4)


# print(table.name)
# print(table.projectionFields)
# print(table.condition)
# print(uncategorized)



query = 'SELECT {} FROM {} WHERE {}'.format(table.projectionFields, table.name, table.condition)

print(query.replace('[','').replace(']',''))

cv2.imshow('gray', gray)
cv2.imshow('thresh', thresh)
cv2.imshow('removed', removed)
# cv2.imshow('circled', test)

cv2.waitKey(0)
cv2.destroyAllWindows()
