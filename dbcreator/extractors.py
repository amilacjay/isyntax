from dbcreator.models import *
from dbcreator.core import *
from nltk import WordNetLemmatizer


class PrimaryExtractor:
    def execute(self, tagged_sents, chunked_sents, ne_chunked_sents, target, isNEExcluded):
        pass


class SecondaryExtractor:
    def execute(self, entities, isNPEExcluded):
        pass


### Identify Candidate Entities & Attributes

class PossessionBasedExtractor(PrimaryExtractor):
    def execute(self, tagged_sents, chunked_sents, ne_chunked_sents, target, isNEExcluded):

        for sIndex, sent in enumerate(tagged_sents):
            for index, item in enumerate(sent):
                if (item[0] == 'has' or item[0] == 'have'):
                    hIndex = item[2]
                    candidateEntityNames = [chunk for chunk in chunked_sents[sIndex] if chunk[0][2] < hIndex]

                    entityName = candidateEntityNames.pop()

                    candidateAttributeData = [chunk for chunk in chunked_sents[sIndex] if chunk[0][2] > hIndex]

                    attributes = []

                    for chunk in candidateAttributeData:
                        attr = Attribute(chunk)
                        attributes.append(attr)

                    ### Named Entity Recognition

                    ne_entites = []

                    for x in ne_chunked_sents[sIndex]:
                        ne = []
                        for y in x:
                            ne.append(y[0].lower())
                        ne_entites.append(' '.join(ne))


                    entity = Entity(entityName)

                    if(isNEExcluded):
                        if (any(ne not in entity.name().replace('_', ' ').lower() for ne in ne_entites)):
                            target.append(entity)
                            entity.setAttributes(attributes)
                            break
                    else:
                        target.append(entity)
                        entity.setAttributes(attributes)
                        break

                ### Possession Based Extraction

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


                ### Pro-noun Based Extraction

                elif item[1] == 'PRP':
                    pass


#############################################################################################################################################


### Filteration of Entities

class RemoveDuplicateEntities(SecondaryExtractor):
    def execute(self, entities, isNPEExcluded):
        uniqueEntities = []

        wn = WordNetLemmatizer()

        for entity in entities:
            ent = entity.name().lower()
            entLemma = wn.lemmatize(ent)

            check = True
            for e in uniqueEntities:
                uq = e.name().lower()
                uqLemma = wn.lemmatize(uq)

                if uqLemma == entLemma:
                    e.getAttributes().extend(entity.getAttributes())
                    check = False
                    break

            if check:
                uniqueEntities.append(entity)

        entities[:] = uniqueEntities[:]


class RemoveNonPotentialEntities(SecondaryExtractor):
    def execute(self, entities, isNPEExcluded):
        nonPotentialList = csv_reader('../knowledge_base/nonpotential_entities.csv')
        filteredList = []

        if(isNPEExcluded):
            for entity in entities:
                check = True
                for item in nonPotentialList:
                    if (entity.name().lower() == item.lower()) or (item.lower() in entity.name()):
                        check = False

                if check:
                    filteredList.append(entity)

            entities[:] = filteredList[:]


class SuggestRelationshipTypes(SecondaryExtractor):
    def execute(self, entities, isNPEExcluded):

        for i, entity1 in enumerate(entities):
            for j, entity2 in enumerate(entities):
                if(i!=j):
                    atrListE2 = entity2.getAttributes()
                    for atr in atrListE2:
                        if atr.name().lower() == entity1.name().lower():
                            entity1.relationships.append((entity2, atr))


### Fiteration of Attributes

class RemoveDuplicateAttributes(SecondaryExtractor):
    def execute(self, entities, isNPEExcluded):

        for entity in entities:
            attrList = entity.getAttributes()
            compList = []
            for i, attr1 in enumerate(attrList):
                for j, attr2 in enumerate(attrList):
                    if(i!=j and set([i,j]) not in compList and attr1.name() == attr2.name()):
                        attrList.remove(attr2)

                    compList.append(set([i,j]))

            for attr in attrList:
                if attr.name() == ('%' or '#' or '$' or '&' or '*' or '@'):
                    attrList.remove(attr)


class UniqueKeyExtractor(SecondaryExtractor):
    def execute(self, entities, isNPEExcluded):
        for entity in entities:

            for attr in entity.getAttributes():
                isUnique = False
                isPrimaryKey = False
                isNotNull = False
                tempData = []
                for i, word in enumerate(attr.data):
                    if(word[0].lower() in ['unique','uniquely','distinguishable','distinguishes','distinct']):
                        isUnique = True
                        isPrimaryKey = True
                        isNotNull = True
                    else:
                        tempData.append(word)
                attr.data = tempData
                attr.isUnique = isUnique
                attr.isPrimaryKey = isPrimaryKey
                attr.isNotNull = isNotNull


class IdentifyAttributeDataType(SecondaryExtractor):
    def execute(self, entities, isNPEExcluded):

        intList = ['number', 'no', 'id', 'SSN', 'code']
        dateList = ['date', 'dob']
        doubleList = ['temperature', 'price', 'distance', 'weight', 'fee', 'volume']

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









        # uniqueAttributes = []
        # for attr in attrList:
        #         check = True
        #         for a in uniqueAttributes:
        #             print(a.name())
        #             if a.name() == attr.name() or attr.name() == '%':
        #                 check = False
        #                 break
        #
        #     if check:
        #         uniqueAttributes.append(attr)
        #
        # attrList[:] = uniqueAttributes[:]



        # uniqueAttributes = []
        #
        # for entity in entities:
        #     check = True
        #     attrList = entity.getAttributes()
        #     for attr in attrList:
        #         if attr.name().lower() == entity.name().lower():
        #             check = False
        #             uniqueAttributes.remove(attr)
        #             print(attr.name())
        #             break
        #
        #     if check:
        #         uniqueAttributes.append(attr)
        #
        # attrList[:] = uniqueAttributes[:]


# class RemoveAttributesFromEntityList(SecondaryExtractor):
#     def execute(self, entities, isNPEExcluded):
#
#         removingIndex = []
#         for entity in entities:
#             attrList = entity.getAttributes()
#             for attr in attrList:
#                 for i, ent in enumerate(entities):
#                     if(attr.name() == ent.name()):
#                         removingIndex.append(i)
#
#         for i in set(removingIndex):
#             e = entities[i]
#             # print(e.name())
#             # entities.remove(e)





















