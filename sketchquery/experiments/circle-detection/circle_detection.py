import cv2
import numpy as np
import math
from sketchquery.core import *

multishapes = '../../samples/elements/extra/multi-shapes.png'
circular = '../../samples/elements/circle/hand-drawn-circles(open).png'

image = cv2.imread(circular, cv2.IMREAD_COLOR)

image2 = np.ones(image.shape)*255

ratio, resized = optimalSize(image, sqr=800)

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)


ret, conts, hierarchy = cv2.findContours(thresh.copy(),method=cv2.CHAIN_APPROX_SIMPLE,mode=cv2.RETR_EXTERNAL)

for c in conts:
    # cv2.drawContours(image,[c],0,(0,255,0), 2)

    hull = cv2.convexHull(c)

    x,y,w,h = cv2.boundingRect(hull)
    # cv2.rectangle(image2, (x,y), (x+w,y+h), (0,255,0),2)

    area = cv2.contourArea(hull)
    arcLength = cv2.arcLength(hull, True)

    calc = math.pow(arcLength, 2) / area

    diff = calc - (math.pi*4)




    cv2.drawContours(image2,[hull],0,(255,0,0),1)
    cv2.drawContours(image,[hull],0,(0,255,0),2)

    cv2.putText(image2, 'Area: '+str(area), (x, y-40), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
    cv2.putText(image2, 'Arc Length: '+str(arcLength), (x, y-25), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
    cv2.putText(image2, 'Ratio: '+str(calc), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)

    # approx = cv2.approxPolyDP()

cv2.imshow('thresh', thresh)
cv2.imshow('final', image2)
cv2.imshow('image', image)


cv2.waitKey(0)
cv2.destroyAllWindows()