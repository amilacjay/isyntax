import cv2
import numpy as np
from sketchquery.core import *
from sketchquery.model import *

rootPath = 'samples/elements/joins/'
file = 'perfect-shapes2.png'
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

# list of lists [text, category, stat, centroid, ptsOfCircle]
tableList = []
columnLists = []
conditionLists = []
variableList = []

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
            if(hier[0][c][2]==-1  and cv2.pointPolygonTest(cont, (stat[cv2.CC_STAT_LEFT], stat[cv2.CC_STAT_TOP]), False)==1):

                center, radius = cv2.minEnclosingCircle(cont)
                ptsInEncCircle = getPointsOfCircle((int(center[0]), int(center[1])), int(radius), resized.shape)
                centroid = getCentroid(cont)

                tableList.append([ELEMENT_TYPE.TABLE, text, stat, centroid, ptsInEncCircle])


pairSet = []
r = resized.copy()
for i, iTable in enumerate(tableList):
    for j, jTable in enumerate(tableList):
        if (i != j and {i, j} not in pairSet):
            pairSet.append({i, j})
            pts = getCommonPoints(iTable[4], jTable[4])
            if(len(pts)==2):
                print(iTable[1] + ' JOIN ' + jTable[1])

                for pt in pts:
                    cv2.circle(r, (pt[0][0], pt[0][1]), 2, (0, 255, 0), 2)


# pts = getCommonPoints(tableList[0][4], tableList[1][4])

# r = resized.copy()
# # pts.dtype = np.int32
#
# for pt in pts:
#     cv2.circle(r, (pt[0][0], pt[0][1]), 2, (0, 255, 0), 2)
#
cv2.imshow('test', r)


cv2.waitKey(0)
cv2.destroyAllWindows()





# print(hier)








# cv2.imshow('Original', image)
# cv2.imshow('Resized', resized)
# cv2.imshow('Grayscale', resized)
# cv2.imshow('Binary', resized)
#
#
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()