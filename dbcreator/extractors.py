from dbcreator.models import *

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
                tempData = []
                for i, word in enumerate(attr.data):
                    if(word[0].lower() in ['unique','distinguishable']):
                        isUnique = True
                    else:
                        tempData.append(word)
                attr.data = tempData
                attr.isUnique = isUnique






