import cv2
import numpy as np
import tesserocr

import pymysql
from PIL import Image
import math
from xml.etree.ElementTree import Element, SubElement, ElementTree

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

    imageArea = threshImg.shape[0]*threshImg.shape[1]
    minArea = imageArea * 0.00004
    maxArea = imageArea * 0.00125

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

    # cv2.imwrite('4.png', labels)

    # dilating components and clustering texts
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
    dilatedText = cv2.morphologyEx(labels.astype(np.uint8), cv2.MORPH_DILATE, kernel)

    # cv2.imwrite('5.png', dilatedText)

    # finding text clusters
    ret = cv2.connectedComponentsWithStats(dilatedText)

    noOfLabels = ret[0]
    labels = ret[1]
    stats = ret[2]
    centroids = ret[3]

    textParts = []

    # loop through text clusters without background(0)
    for i in range(1, noOfLabels, 1):
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

def eucDist(point1, point2):
    return math.sqrt(pow(point1[0]-point2[0], 2) + pow(point1[1]-point2[1], 2))

def getPointsOfCircle(center, radius, shape):
    mask = np.zeros(shape, np.uint8)
    cv2.circle(mask, center, radius, 255, 2)

    where = np.argwhere(mask == 255)
    return where

def getCommonPoints(points1, points2):
    commonPts = []
    for pt1 in points1:
        for pt2 in points2:
            if pt1[0] == pt2[0] and pt1[1]==pt2[1]:

                commonPts.append([[pt1[1], pt1[0]]])


    return np.array(commonPts)

def getCentroid(contour):
    M = cv2.moments(contour)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    return (cx, cy)

def toPoints(stat):
    return [(stat[cv2.CC_STAT_LEFT], stat[cv2.CC_STAT_TOP]),
            (stat[cv2.CC_STAT_LEFT]+stat[cv2.CC_STAT_WIDTH],
             stat[cv2.CC_STAT_TOP]+stat[cv2.CC_STAT_HEIGHT])]

def scale(cont, ratio):
    cx, cy = getCentroid(cont)

    newCont = []

    for [[x, y]] in cont:
        X = x
        Y = y
        if(x>cx):
            X += abs(x-cx)*(ratio-1)
        if(y>cy):
            Y += abs(y-cy)*(ratio-1)
        if(x<cx):
            X -= abs(x-cx)*(ratio-1)
        if(y<cy):
            Y -= abs(y-cy)*(ratio-1)

        newCont.append([[int(X), int(Y)]])

    return np.array(newCont)

def getPointsOfRect(stat, shape):
    mask = cv2.cvtColor(np.zeros(shape, dtype=np.uint8), cv2.COLOR_BGR2GRAY)
    cv2.rectangle(mask, toPoints(stat)[0], toPoints(stat)[1], 255)
    ret, conts, hier = cv2.findContours(mask, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

    return conts[0]

def schemaTree():
    connection = pymysql.connect(host='localhost',
                                 user=self.user,
                                 password=self.passwd,
                                 db=self.db,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # forming an XML
            root = Element('database')
            root.set('dbname', self.db)
            tree = ElementTree(root)
            tablesElement = Element('tables')
            root.append(tablesElement)

            # Using Cursor to fetch data as SQL queries
            cursor.execute("SHOW TABLES")
            connection.commit()
            tables = cursor.fetchall()
            for table in tables:
                tablekeyList = sorted(list(table.keys()))
                tableSubElement = SubElement(tablesElement, "table")
                tableSubElement.set('tbname', str(table[tablekeyList[0]]))
                cursor.execute("select table_name, column_name, data_type, character_maximum_length, column_key "
                               "from INFORMATION_SCHEMA.COLUMNS "
                               "where table_name = '"+table[tablekeyList[0]]+"' AND TABLE_SCHEMA = '"+self.db+"';")
                atts = cursor.fetchall()
                connection.commit()
                attsSubElement = SubElement(tableSubElement, "attributes")
                for att in atts:
                    attKeyList = sorted(list(att.keys()))
                    attSubElement = SubElement(attsSubElement, "attribute")
                    dataTypeSubElement = SubElement(attSubElement, "dataType")
                    lengthSubElement = SubElement(attSubElement, "maxLength")
                    columnKeyElement = SubElement(attSubElement, "columnKey")
                    refTableSubElement = SubElement(attSubElement, "referencedTable")
                    refColumnSubElement = SubElement(attSubElement, "referencedColumn")
                    valuesSubElement = SubElement(attSubElement, "values")
                    attSubElement.set('attname', str(att[attKeyList[2]]))
                    dataTypeSubElement.text = str(att[attKeyList[3]])
                    lengthSubElement.text = str(att[attKeyList[0]])
                    columnKeyElement.text = str(att[attKeyList[1]])
                    cursor.execute("SELECT table_name,column_name,referenced_table_name,referenced_column_name "
                                   "FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE "
                                   "WHERE column_name = '" + str(att[attKeyList[2]]).lower() + "' AND table_name = '" + str(
                        table[tablekeyList[
                            0]]).lower() + "' AND referenced_column_name IS NOT NULL AND CONSTRAINT_SCHEMA = '" + self.db + "';")
                    foreigns = cursor.fetchall()
                    connection.commit()

                    cursor.execute("SELECT " + str(att[attKeyList[2]]) + " FROM " + str(table[tablekeyList[0]]))
                    dataSet = cursor.fetchall()
                    connection.commit()

                    i = 1
                    for data in dataSet:
                        dataSubElement = SubElement(valuesSubElement, "data")
                        dataSubElement.set('id', str(i))
                        if data:
                            dataSubElement.text = str(data[str(att[attKeyList[2]])])
                            i += 1

                    for foreign in foreigns:
                        foreignKeyList = sorted(list(foreign.keys()))
                        if foreign:
                            refTableSubElement.text = foreign[foreignKeyList[2]]
                            refColumnSubElement.text = foreign[foreignKeyList[1]]
            return tree
    finally:
        connection.close()



def convertToSQL(queryList):

    queryStatementList = []

    for query in queryList:
        tableName = ''
        conditionStr = ''
        projectionStr = '*'

        # if(query.projection[0] != ''):
        #     projectionStr = query.projection[0].replace('[', '').replace(']', '').replace(' ','')


        if len(query.tables)==1:
            tableName = query.tables[0]
            template = ''
            if len(query.conditions) > 0:
                conditionStr = ' AND '.join([condition.replace('&&', 'AND').replace('==', '=').replace('||', 'OR') for condition in query.conditions])
                template = "SELECT {} FROM {} WHERE {}"

            else:
                template = "SELECT {} FROM {}"

            statement = template.format(projectionStr, tableName, conditionStr)
            print(statement)
            queryStatementList.append(statement.replace("'","\"").replace("‘", "\""))


        if len(query.tables)==2:
            if len(query.conditions) > 0:
                conditionStr = ' AND '.join(
                    [condition.replace('&&', 'AND').replace('==', '=').replace('||', 'OR') for condition in
                     query.conditions])

            template = "SELECT {} FROM {} INNER JOIN {} ON {}"
            statement = template.format(projectionStr, query.tables[0], query.tables[1], conditionStr)
            print(statement)
            queryStatementList.append(statement.replace("'", "\"").replace("‘", "\""))

    if len(queryStatementList)==1:
        return queryStatementList[0]


    for i, query in enumerate(queryList):
        print("Query : " + str(i + 1))
        print('tables : ' + str(query.tables))
        print('condition : ' + str(query.conditions))
        print('projection : ' + str(query.projection))

    return "SELECT * FROM hotel"

