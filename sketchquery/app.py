import cv2
import numpy as np
from sketchquery.core import *
from sketchquery.model import *
import logging

logger = logging.getLogger('iSyntax Logger')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('[%(levelname)s]\tat line %(lineno)s\t%(asctime)s:\t%(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)

class SketchQueryApp:

    def __init__(self, filePath, detailedImage=True, stepImages=False, tree=None):
        self.filePath = filePath
        self.detailedImage = detailedImage
        self.stepImages = stepImages
        self.schemaTree = tree

    def run(self):

        logger.info("""
          _  _____             _
         (_)/ ____|           | |
          _| (___  _   _ _ __ | |_ __ ___  __
         | |\___ \| | | | '_ \| __/ _` \ \/ /
         | |____) | |_| | | | | || (_| |>  <
         |_|_____/ \__, |_| |_|\__\__,_/_/\_|
                    __/ |
                   |___/
         Natural Language Interface for Databases | Version 1.0
         Sketch Query Module

         Final Year Research Project
         Faculty of Information Technology
         University of Moratuwa
                   """)

        logger.info("reading image file : " + self.filePath)
        image = cv2.imread(self.filePath, cv2.IMREAD_COLOR)

        resizingSquare = 700
        logger.info("resizing image into "+ str(resizingSquare) + " square")
        ratio, resized = optimalSize(image, sqr=resizingSquare)

        logger.info("converting image from BGR to GRAY")
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

        logger.info("thresholding image")
        thresh = binaryImage(gray)
        removed = thresh.copy()

        logger.info("identifying statistics of text regions")
        textPartsWithStats = textRegionsWithStats(thresh)

        # list of tuples (text, stat)
        textAndStats = []

        logger.info("iterating text regions and OCR them")
        for textPartWithStat in textPartsWithStats:
            textPart = textPartWithStat[0]
            ## 0:left(x), 1:top(y), 2:H, 3:W, 4:Area
            stat = textPartWithStat[1]

            text = imageToText(textPart).strip()
            textAndStats.append((text, stat))

            removed[stat[cv2.CC_STAT_TOP]:stat[cv2.CC_STAT_TOP] + stat[cv2.CC_STAT_HEIGHT], stat[cv2.CC_STAT_LEFT]:stat[cv2.CC_STAT_LEFT] + stat[cv2.CC_STAT_WIDTH]] = 0


        logger.info("finding contours in text-removed image")
        ret, conts, hier = cv2.findContours(removed.copy(), mode=cv2.RETR_CCOMP, method=cv2.CHAIN_APPROX_SIMPLE)

        # cv2.drawContours(resized, conts, -1, (0, 255, 0), 2)

        # list of lists [text, category, stat, centroid, ptsOfCircle]
        simpleTableList = []
        joinedTableList = []
        columnLists = []
        conditionLists = []
        variableList = []
        operatorsList = ['=', '<', '>', '<=', '>=', '&&', '||', '&', '|', '!']

        elements = []
        queryList = []

        logger.info("iterating texts and identifying their category")
        for i, tas in enumerate(textAndStats):
            text = tas[0]
            stat = tas[1]
            # print(text)

            if text.startswith('[') and text.endswith(']'):
                logger.debug("an attribute list was identified: " + text)

                columnLists.append([ELEMENT_TYPE.COL_LIST, text.replace('[', '').replace(']', '').replace(' ', '').split(','), stat])
                cv2.rectangle(resized, toPoints(stat)[0], toPoints(stat)[1], (0, 0, 255))
                pointsOfRect = getPointsOfRect(stat, resized.shape)
                scaledUp = scale(pointsOfRect, 1.2)
                cv2.drawContours(resized, [scaledUp], -1, (255, 0, 0))

                elements.append([3, text, scaledUp])


            elif any(op in text for op in operatorsList):
                logger.debug("a condition was identified: " + text)

                conditionLists.append([ELEMENT_TYPE.CONDITION, text, stat])
                cv2.rectangle(resized, toPoints(stat)[0], toPoints(stat)[1], (0, 0, 255))
                pointsOfRect = getPointsOfRect(stat, resized.shape)
                scaledUp = scale(pointsOfRect, 1.2)
                cv2.drawContours(resized, [scaledUp], -1, (255, 0, 0))

                elements.append([2, text, scaledUp])

            elif text.startswith('$'):
                logger.debug("a variable was identified: " + text)

                variableList.append([ELEMENT_TYPE.VARIABLE, text, stat])
                cv2.rectangle(resized, toPoints(stat)[0], toPoints(stat)[1], (0, 0, 255))
                pointsOfRect = getPointsOfRect(stat, resized.shape)
                scaledUp = scale(pointsOfRect, 1.2)
                cv2.drawContours(resized, [scaledUp], -1, (255, 0, 0))

                elements.append([4, text, scaledUp])

            else:
                for c, cont in enumerate(conts):
                    # cv2.drawContours(resized, conts, c, (0, 255, 0), 2)
                    # cv2.imshow('Resized', resized)
                    # cv2.waitKey(0)

                    if(hier[0][c][2]==-1  and cv2.pointPolygonTest(cont, (stat[cv2.CC_STAT_LEFT], stat[cv2.CC_STAT_TOP]), False)==1):
                        logger.debug("a table is identified: '{}'".format(text))

                        area = cv2.contourArea(cont)
                        arcLength = cv2.arcLength(cont, True)
                        ratio = math.pow(arcLength, 2) / area
                        cv2.drawContours(resized, [cont], -1, (0, 255, 0), 1)
                        centroid = getCentroid(cont)

                        print(ratio)
                        if (ratio <= 16):
                            logger.debug("categorized the table '{}' as SIMPLE_TABLE".format(text))

                            scaledUp = scale(cont, 1.2)
                            cv2.drawContours(resized, [scaledUp], -1, (255, 0, 0), 1)
                            simpleTableList.append([ELEMENT_TYPE.SIMPLE_TABLE, text, stat, centroid, -1, scaledUp])
                            # take the parent from the hierarchy
                            parent = conts[hier[0][c][3]]
                            # remove the circle
                            cv2.drawContours(removed, [parent], -1, 0, cv2.FILLED)

                            elements.append([0, text, scaledUp])
                            query = Query()
                            query.tables.append(text)
                            queryList.append(query)

                        else:
                            logger.debug("categorized the table '{}' as JOINED_TABLE".format(text))

                            scaledUp = scale(cont, 1.2)
                            cv2.drawContours(resized, [scaledUp], -1, (255, 0, 0), 1)
                            center, radius = cv2.minEnclosingCircle(cont)
                            ptsInEncCircle = getPointsOfCircle((int(center[0]), int(center[1])), int(radius), resized.shape)
                            joinedTableList.append([ELEMENT_TYPE.JOINED_TABLE, text, stat, centroid, ptsInEncCircle])
                            # take the parent from the hierarchy
                            parent = conts[hier[0][c][3]]
                            # remove joined circles
                            cv2.drawContours(removed, [parent], -1, 0, cv2.FILLED)

                            elements.append([1, text, scaledUp])

        logger.info("element identification finished")

        logger.info("simple table list: " + str([s[1] for s in simpleTableList]))
        logger.info("joined table list: " + str([j[1] for j in joinedTableList]))
        logger.info("conditions list: " + str([j[1] for j in conditionLists]))
        logger.info("projection list: " + str([j[1] for j in columnLists]))

        logger.info("checking for joined table combinations")
        pairSet = []
        r = resized.copy()
        for i, iTable in enumerate(joinedTableList):
            for j, jTable in enumerate(joinedTableList):
                if (i != j and {i, j} not in pairSet):
                    pairSet.append({i, j})
                    pts = getCommonPoints(iTable[4], jTable[4])
                    if(len(pts)>=2):
                        logger.debug(iTable[1] + ' JOIN ' + jTable[1])
                        query = Query()
                        query.tables.append(iTable[1])
                        query.tables.append(jTable[1])
                        queryList.append(query)

                        for pt in pts:
                            cv2.circle(resized, (pt[0][0], pt[0][1]), 2, (0, 255, 0), 2)


        logger.info("joined table combination checking finished")

        logger.info("finding contours for arrows(connectors) in element and text free image")
        ret, arrowConts, aHier = cv2.findContours(removed.copy(), mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(resized, arrowConts, -1, (0, 255, 0), 1)

        logger.info("checking for connected elements by each arrow")
        for ac in arrowConts:
            rect = cv2.minAreaRect(ac)
            box = cv2.boxPoints(rect)
            box = np.int0(box)

            rbox = scale(np.array([[b] for b in box]), 2)

            table = other = '  '

            for el in elements:
                    boundary = el[2]


                    if any([pt] for [pt] in boundary if cv2.pointPolygonTest(rbox, (pt[0], pt[1]), False)==1) or any([pt] for [pt] in rbox if cv2.pointPolygonTest(boundary, (pt[0], pt[1]), False) == 1):
                        if(el[0] in [0, 1]):
                            table = el
                        else:
                            other = el

            for query in queryList:
                # print(table[1])
                if(table[1] in query.tables):
                    if other != None:
                        if other[0] == 2:
                            query.conditions.append(other[1])
                        elif other[0] == 3:
                            query.projection.append(other[1])

            cv2.drawContours(resized, [box], 0, (0, 0, 255), 1)
            cv2.drawContours(resized, [rbox], 0, (255, 0, 0), 1)



        # for i, query in enumerate(queryList):
        #     print("Query : " + str(i+1))
        #     print('tables : ' + str(query.tables))
        #     print('condition : ' + str(query.conditions))
        #     print('projection : ' + str(query.projection))


        sql = convertToSQL(queryList)


        if(self.stepImages):
            logger.info("showing resulting images...")
            cv2.imshow('Grayscale', gray)
            cv2.imshow('test', r)
            cv2.imshow('removed', removed)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


        if(self.detailedImage):
            cv2.imshow('resized', resized)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


        logger.info("Sketch Query module was finished successfully!")
        return sql

if __name__ == "__main__":
    app = SketchQueryApp(filePath='samples/sketches/two-queries.png')
    app.run()