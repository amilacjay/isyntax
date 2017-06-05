import cv2
import numpy as np
from sketchquery.core import *
from sketchquery.model import *

image = cv2.imread('../samples/sketches/joined-sketch.png', cv2.IMREAD_COLOR)
ratio, resized = optimalSize(image, sqr=600)
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
    cv2.imshow('T'+str(i), textPart)

    removed[stat[1]:stat[1] + stat[3], stat[0]:stat[0] + stat[2]] = 0

    ret, conts, hier = cv2.findContours(removed.copy(), mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

    isEnclosedByCircle, hull = enclosedByCircle(stat, conts)

    if(isEnclosedByCircle):
        cv2.drawContours(removed, [hull], 0, 0, cv2.FILLED)

    ret, conts, hier = cv2.findContours(removed.copy(), mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

    x = cv2.cvtColor(removed.copy(), cv2.COLOR_GRAY2BGR)

    for c in conts:
        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        # centroid of the min area rectangle
        try:
            M = cv2.moments(box)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(x, (cX, cY), 7, (0, 0, 255), -1)

            # centroid of the contour(arrow)
            M2 = cv2.moments(c)
            cX2 = int(M2["m10"] / M2["m00"])
            cY2 = int(M2["m01"] / M2["m00"])
            cv2.circle(x, (cX2, cY2), 7, (255, 0, 0), -1)

            cv2.drawContours(x, [box], 0, (0, 255, 0), 2)
        except:
            pass

    # cv2.imwrite('14.png', x)

    if text.startswith('[') and text.endswith(']'):
        projectionFields = text.replace('[','').replace(']','').replace(' ','').split(',')
        table.setProjectionFields(projectionFields)

    elif '=' in text:
        table.setCondition(text)

    elif isEnclosedByCircle:
        table.name = text

    else:
        uncategorized.append(textPart)




query = 'SELECT {} FROM {} WHERE {}'.format(', '.join(table.projectionFields), table.name, table.condition)

print(query)

cv2.imshow('gray', gray)
cv2.imshow('thresh', thresh)
cv2.imshow('removed', removed)
# cv2.imshow('circled', experiments)

cv2.waitKey(0)
cv2.destroyAllWindows()
