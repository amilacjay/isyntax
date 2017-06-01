import cv2
import numpy as np
import tesserocr
from PIL import Image
import math

def optimalSize(img, sqr=800):
    height, width = img.shape[:2]

    ratio = height/width

    if(ratio<=1):
        h = ratio * sqr
        w = sqr
    else:
        h = sqr
        w = (1/ratio) * sqr

    scaledRatio = h/height

    output = cv2.resize(img, None, fx=w/width, fy=h/height, interpolation = cv2.INTER_CUBIC)
    return scaledRatio, output

def binaryImage(grayImg):
    ret, thresh = cv2.threshold(grayImg, 127, 255, cv2.THRESH_BINARY_INV)
    return thresh

def textRegionsWithStats(threshImg, minArea=10, maxArea=300):

    ret = cv2.connectedComponentsWithStats(threshImg)

    noOfLabels = ret[0]
    labels = ret[1]
    stats = ret[2]
    centroids = ret[3]

    # removing too large and too small components
    for i in range(1, ret[0], 1):
        comp = stats[i]

        if comp[4] > maxArea or comp[4] < minArea:
            labels[labels == i] = 0

    labels[labels > 0] = 255

    cv2.imwrite('4.png', labels)

    # dilating components and clustering texts
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
    dilatedText = cv2.morphologyEx(labels.astype(np.uint8), cv2.MORPH_DILATE, kernel)

    cv2.imwrite('5.png', dilatedText)

    # finding text clusters
    ret = cv2.connectedComponentsWithStats(dilatedText)

    noOfLabels = ret[0]
    labels = ret[1]
    stats = ret[2]
    centroids = ret[3]

    textParts = []

    # loop through text clusters without background(0)
    for i in range(1, ret[0], 1):
        comp = stats[i]
        crop = threshImg[comp[1]:comp[1] + comp[3], comp[0]:comp[0] + comp[2]]
        textParts.append((crop,comp))

    return textParts

def imageToText(img):
    pilImage = Image.fromarray(img)
    return tesserocr.image_to_text(pilImage).replace('\n', '')

def enclosedByCircle(textRegionStat, contours):

    # take the coordinates(top-left corner and bottom-right corner) of the textRegion
    textX1 = textRegionStat[0]
    textX2 = textRegionStat[0]+textRegionStat[2]
    textY1 = textRegionStat[1]
    textY2 = textRegionStat[1]+textRegionStat[3]

    # loop through each contour
    for cont in contours:

        # take the convex hull of the contour to close the opened circular shapes
        hull = cv2.convexHull(cont)

        # calculate the ratio, (perimeter)^2 / (area)
        area = cv2.contourArea(hull)
        arcLength = cv2.arcLength(hull, True)
        if area == 0:
            continue

        ratio = math.pow(arcLength, 2) / area

        # if it is perfect circle ratio value should be 12.566..
        # in order to be a closer shape to circle, values should be less than or equal to 14 (assumption)
        isCircle = (ratio <= 14)

        # calculate the centroid point's coordinate using image moments
        M = cv2.moments(hull)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])

        # check for the existance of the centroid point within the text region
        isEnclosed = cx >= textX1 and cx <= textX2 and cy >= textY1 and cy <= textY2

        if(isEnclosed):
            return True, hull


    return False, None