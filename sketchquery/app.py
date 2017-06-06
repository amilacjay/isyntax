import cv2
import numpy as np
from sketchquery.core import *
from sketchquery.model import *

rootPath = 'samples/sketches/'
file = 'simplequery.png'
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
simpleTableList = []
joinedTableList = []
columnLists = []
conditionLists = []
variableList = []
operatorsList = ['==', '<', '>', '<=', '>=', '&&', '||', '&', '|', '!']


for i, tas in enumerate(textAndStats):
    text = tas[0]
    stat = tas[1]

    if text.startswith('[') and text.endswith(']'):
        columnLists.append([ELEMENT_TYPE.COL_LIST, text.replace('[', '').replace(']', '').replace(' ', '').split(','), stat])
        cv2.rectangle(resized, toPoints(stat)[0], toPoints(stat)[1], (0, 0, 255))

    elif any(op in text for op in operatorsList):
        conditionLists.append([ELEMENT_TYPE.CONDITION, text, stat])
        cv2.rectangle(resized, toPoints(stat)[0], toPoints(stat)[1], (0, 0, 255))

    elif text.startswith('$'):
        variableList.append([ELEMENT_TYPE.VARIABLE, text, stat])

    else:
        for c, cont in enumerate(conts):
            # cv2.drawContours(resized, conts, c, (0, 255, 0), 2)
            # cv2.imshow('Resized', resized)
            # cv2.waitKey(0)

            if(hier[0][c][2]==-1  and cv2.pointPolygonTest(cont, (stat[cv2.CC_STAT_LEFT], stat[cv2.CC_STAT_TOP]), False)==1):

                area = cv2.contourArea(cont)
                arcLength = cv2.arcLength(cont, True)
                ratio = math.pow(arcLength, 2) / area
                cv2.drawContours(resized, [cont], -1, (0, 255, 0), 1)
                centroid = getCentroid(cont)
                print(ratio)

                if (ratio <= 15):

                    parent = conts[hier[0][c][3]]

                    scaledUp = scale(cont, 1.2)
                    cv2.drawContours(resized, [scaledUp], -1, (255, 0, 0), 1)
                    simpleTableList.append([ELEMENT_TYPE.TABLE, text, stat, centroid, -1, scaledUp])
                    cv2.drawContours(removed, [parent], -1, 0, cv2.FILLED)

                else:
                    center, radius = cv2.minEnclosingCircle(cont)
                    ptsInEncCircle = getPointsOfCircle((int(center[0]), int(center[1])), int(radius), resized.shape)


                    joinedTableList.append([ELEMENT_TYPE.JOINED_TABLE, text, stat, centroid, ptsInEncCircle])
                    parent = conts[hier[0][c][3]]
                    cv2.drawContours(removed, [parent], -1, 0, cv2.FILLED)


for s in simpleTableList:
    print('Simple Table: ' + s[1])

for j in joinedTableList:
    print('Joined Table: ' + j[1])

pairSet = []
r = resized.copy()
for i, iTable in enumerate(joinedTableList):
    for j, jTable in enumerate(joinedTableList):
        if (i != j and {i, j} not in pairSet):
            pairSet.append({i, j})
            pts = getCommonPoints(iTable[4], jTable[4])
            if(len(pts)>=2):
                print(iTable[1] + ' JOIN ' + jTable[1])

                for pt in pts:
                    cv2.circle(resized, (pt[0][0], pt[0][1]), 2, (0, 255, 0), 2)


ret, arrowConts, aHier = cv2.findContours(removed.copy(), mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(resized, arrowConts, -1, (0, 255, 0), 1)


for ac in arrowConts:
    rect = cv2.minAreaRect(ac)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    rbox = scale(np.array([[b] for b in box]), 1.2)

    for tbl in simpleTableList:
        boundary = tbl[5]
        for [p] in boundary:
            if cv2.pointPolygonTest(rbox, (p[0], p[1]), False)==1:
                cv2.circle(resized, (p[0], p[1]), 2, (0,0,0), 2)


    cv2.drawContours(resized, [box], 0, (0, 0, 255), 1)
    cv2.drawContours(resized, [rbox], 0, (255, 0, 0), 1)


# cv2.imshow('Original', image)
# cv2.imshow('Grayscale', gray)
cv2.imshow('resized', resized)
# cv2.imshow('test', r)
# cv2.imshow('removed', removed)
#
cv2.waitKey(0)
cv2.destroyAllWindows()