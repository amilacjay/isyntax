import cv2
import numpy as np
from sketchquery.core import *
from sketchquery.model import *

rootPath = '../../samples/sketches/'
file = 'join-report-experiment2.png'
fullPath = rootPath+file

image = cv2.imread(fullPath, cv2.IMREAD_COLOR)
atio, resized = optimalSize(image, sqr=600)
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
thresh = binaryImage(gray)
removed = thresh.copy()
textPartsWithStats = textRegionsWithStats(thresh)

# list of tuples (text, stat)
textAndStats = []



for i in range(len(textPartsWithStats)):
    textPart = textPartsWithStats[i][0]
    ## 0:left(x), 1:top(y), 2:H, 3:W, 4:Area
    stat = textPartsWithStats[i][1]
    text = imageToText(textPart).strip()
    textAndStats.append((text, stat))
    removed[stat[cv2.CC_STAT_TOP]:stat[cv2.CC_STAT_TOP] + stat[cv2.CC_STAT_HEIGHT], stat[cv2.CC_STAT_LEFT]:stat[cv2.CC_STAT_LEFT] + stat[cv2.CC_STAT_WIDTH]] = 0


ret, conts, hier = cv2.findContours(removed.copy(), mode=cv2.RETR_CCOMP, method=cv2.CHAIN_APPROX_SIMPLE)

# cv2.drawContours(resized, conts, -1, (0, 255, 0), 2)

# list of lists [text, category, stat, centroid, ptsOfCircle]
tableList = []
columnLists = []
conditionLists = []
variableList = []
r = resized.copy()

for i, tas in enumerate(textAndStats):
    text = tas[0]
    stat = tas[1]

    if text.startswith('[') and text.endswith(']'):
        columnLists.append([ELEMENT_TYPE.COL_LIST, text.replace('[', '').replace(']', '').replace(' ', '').split(','), stat])

    elif ('=' in text) or ('&&' in text) or ('||' in text):
        conditionLists.append([ELEMENT_TYPE.CONDITION, text, stat])

    elif text.startswith('$'):
        variableList.append([ELEMENT_TYPE.VARIABLE, text, stat])

    else:
        for c, cont in enumerate(conts):
            # cv2.drawContours(resized, conts, c, (0, 255, 0), 2)
            # cv2.imshow('Resized', resized)
            # cv2.waitKey(0)
            if(hier[0][c][2]==-1  and cv2.pointPolygonTest(cont, (stat[cv2.CC_STAT_LEFT], stat[cv2.CC_STAT_TOP]), False)==1):

                center, radius = cv2.minEnclosingCircle(cont)

                cv2.circle(r, (int(center[0]), int(center[1])), int(radius), (0, 255, 0), 2)

                ptsInEncCircle = getPointsOfCircle((int(center[0]), int(center[1])), int(radius), resized.shape)
                centroid = getCentroid(cont)

                tableList.append([ELEMENT_TYPE.TABLE, text, stat, centroid, ptsInEncCircle])
                parent = conts[hier[0][c][3]]
                cv2.drawContours(removed, [parent], -1, 0, cv2.FILLED)



pairSet = []

for i, iTable in enumerate(tableList):
    for j, jTable in enumerate(tableList):
        if (i != j and {i, j} not in pairSet):
            pairSet.append({i, j})
            pts = getCommonPoints(iTable[4], jTable[4])
            if(len(pts)>=2):
                print(iTable[1] + ' JOIN ' + jTable[1])

                for pt in pts:
                    cv2.circle(r, (pt[0][0], pt[0][1]), 2, (0, 0, 255), 1)


# cv2.imshow('resized', resized)
cv2.imshow('test', r)
# cv2.imshow('removed', removed)
#
#
cv2.waitKey(0)
cv2.destroyAllWindows()