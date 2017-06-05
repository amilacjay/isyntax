from dbcreator.models import *
from dbcreator.core import csv_reader

class PrimaryExtractor:
    def execute(self, tagged_sents, chunked_sents, target):
        pass


class SecondaryExtractor:
    def execute(self, entities):
        pass


class PossessionBasedExtractor(PrimaryExtractor):
    def execute(self, tagged_sents, chunked_sents, target):

        for sIndex, sent in enumerate(tagged_sents):

            for index, item in enumerate(sent):
                if ((item[0] == 'has' or item[0] == 'have')):
                    hIndex = item[2]
                    candidateEntityNames = [chunk for chunk in chunked_sents[sIndex] if chunk[0][2]<hIndex]

                    entityName = candidateEntityNames.pop()

                    candidateAttributeData = [chunk for chunk in chunked_sents[sIndex] if chunk[0][2]>hIndex]

                    attributes = []

                    for chunk in candidateAttributeData:
                        attr = Attribute(chunk)
                        attributes.append(attr)

                    entity = Entity(entityName)
                    entity.setAttributes(attributes)
                    target.append(entity)
                    break

                if ((item[1] == 'PRP')):
                    pass


                elif item[1] == 'POS':
                    posIndex = sent[index-1][2]
                    candidateAttributeData = [chunk for chunk in chunked_sents[sIndex] if chunk[0][2] > posIndex]
                    attributes = []

                    for chunk in candidateAttributeData:
                        attr = Attribute(chunk)
                        attributes.append(attr)


                    entity = Entity([sent[index-1]])
                    entity.setAttributes(attributes)
                    target.append(entity)
                    break


class UniqueKeyExtractor(SecondaryExtractor):
    def execute(self, entities):
        for entity in entities:

            for attr in entity.getAttributes():
                isUnique = False
                # isPrimaryKey = False
                tempData = []
                for i, word in enumerate(attr.data):
                    if(word[0].lower() in ['unique','distinguishable']):
                        isUnique = True
                        # isPrimaryKey = True
                    else:
                        tempData.append(word)
                attr.data = tempData
                attr.isUnique = isUnique
                # attr.isPrimaryKey = isPrimaryKey


class IdentifyAttributeDataType(SecondaryExtractor):
    def execute(self, entities):

        intList = ['number', 'no', 'id', 'SSN']
        dateList = ['date', 'dob']
        doubleList = ['temperature', 'price', 'distance', 'weight']

        for entity in entities:
            attrList = entity.getAttributes()
            for attr in attrList:
                for item in intList:
                    if item.lower() in attr.name().lower():
                        attr.dtype = DataType.INTEGER
                    if 'phone' in attr.name().lower():
                        attr.dtype = DataType.VARCHAR
                for item in dateList:
                    if item.lower() in attr.name().lower():
                        attr.dtype = DataType.DATETIME
                for item in doubleList:
                    if item.lower() in attr.name().lower():
                        attr.dtype = DataType.DOUBLE


class RemoveDuplicateEntities(SecondaryExtractor):
    def execute(self, entities):
        pass

        compList = []

        for i, entity1 in enumerate(entities):
            for j, entity2 in enumerate(entities):
                if(i!=j and set([i,j]) not in compList and entity1.name() == entity2.name()):
                    entity1.getAttributes().extend(entity2.getAttributes())
                    entities.remove(entity2)

                compList.append(set([i,j]))


class RemoveDuplicateAttributes(SecondaryExtractor):
    def execute(self, entities):
        pass

        compList = []

        for entity in entities:
            attrList = entity.getAttributes()
            for i, attr1 in enumerate(attrList):
                for j, attr2 in enumerate(attrList):
                    if(i!=j and set([i,j]) not in compList and attr1.name() == attr2.name()):
                        attrList.remove(attr2)

                    compList.append(set([i,j]))

            # for attr in attrList:
            #     if attr.name().contains('%'):
            #         ch = attr.name().split('%')



class RemoveAttributesFromEntityList(SecondaryExtractor):
    def execute(self, entities):

        removingIndex = []
        for entity in entities:
            attrList = entity.getAttributes()
            for attr in attrList:
                for i, ent in enumerate(entities):
                    if(attr.name() == ent.name()):
                        removingIndex.append(i)

        for i in set(removingIndex):
            e = entities[i]
            # print(e.name())
            # entities.remove(e)


class PrimaryKeyExtractor(SecondaryExtractor):
    def execute(self, entities):
        for entity in entities:
            for attr in entity.getAttributes():
                if attr in csv_reader('../knowledge_base/primary_keys.csv'):
                    # attr.isPrimaryKey = True
                    # attr.isUnique = True
                     pass
















