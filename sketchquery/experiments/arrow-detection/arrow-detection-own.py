import cv2
import numpy as np
import islib as isx
from QueryModel import *

image = cv2.imread('test/images/cond-arrow-table.jpg', cv2.IMREAD_COLOR)

duplicate = image.copy()

ratio, resized = isx.optimalSize(image, sqr=800)

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

thresh = isx.binaryImage(gray)

removed = thresh.copy()

textPartsWithStats = isx.textRegionsWithStats(thresh)

table = Table()
uncategorized = []

for i in range(len(textPartsWithStats)):
    textPart = textPartsWithStats[i][0]
    textRegionStat = textPartsWithStats[i][1]
    text = isx.imageToText(textPart).strip()
    # cv2.imshow(str(i), textPart)

    textX1 = textRegionStat[0]
    textX2 = textRegionStat[0] + textRegionStat[2]
    textY1 = textRegionStat[1]
    textY2 = textRegionStat[1] + textRegionStat[3]

    removed[textY1:textY2, textX1:textX2] = 0
    cv2.rectangle(duplicate, (textX1,textY1), (textX2, textY2), (0,255,0))


    gutter = int((((textX2-textX1) + (textY2-textY1))/2)*2 * 0.2)

    cv2.rectangle(duplicate, (textX1-gutter, textY1-gutter), (textX2+gutter, textY2+gutter), (0,0,255))



cv2.imshow('original', image)
cv2.imshow('duplicate', duplicate)
cv2.imshow('thresh', thresh)
cv2.imshow('removed', removed)

cv2.waitKey(0)
cv2.destroyAllWindows()