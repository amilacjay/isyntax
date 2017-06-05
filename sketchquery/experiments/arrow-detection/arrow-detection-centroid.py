import cv2
import numpy as np
from sketchquery.core import *
from sketchquery.model import *

rootPath = '../../samples/elements/arrow/'
file = 'experiment.png'
fullPath = rootPath+file

image = cv2.imread(fullPath, cv2.IMREAD_COLOR)
ratio, resized = optimalSize(image, sqr=600)
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
thresh = binaryImage(gray)



ret, arrowConts, aHier = cv2.findContours(thresh.copy(), mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(resized, arrowConts, -1, (0, 255, 0), 1)

print(len(arrowConts))
for ac in arrowConts:
    rect = cv2.minAreaRect(ac)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(resized, [box], 0, (0, 0, 255), 1)
    centroid = getCentroid(ac)
    boxCenter = getCentroid(box)
    cv2.line(resized, boxCenter, centroid, (0, 0, 0), 2)
    cv2.circle(resized, centroid, 2, (0, 0, 255), 2)
    cv2.circle(resized, boxCenter, 2, (255, 0, 0), 2)



cv2.imshow('resized', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()