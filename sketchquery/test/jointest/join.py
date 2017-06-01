import cv2
import numpy as np
from sketchquery.core import *

image = cv2.imread('../../samples/elements/joins/two-circles.jpg', cv2.IMREAD_COLOR)

ratio, resized = optimalSize(image, sqr=800)

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

thresh = binaryImage(gray)

ret, conts, hier = cv2.findContours(thresh.copy(), mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)


hull = cv2.convexHull(conts[0])

cv2.drawContours(image, [hull], -1, (0, 255, 0))

x = cv2.convexityDefects(conts, hull)
print(x)

cv2.imshow('join', image)

cv2.waitKey(0)
cv2.destroyAllWindows()