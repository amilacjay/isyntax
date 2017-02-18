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
            hIndex = 999

            candidateEntityNames = None
            for index, item in enumerate(sent):
                if ((item[0] == 'has' or item[0] == 'have')):
                    hIndex = item[2]
                    candidateEntityNames = [chunk for chunk in chunked_sents[sIndex] if chunk[0][2]<hIndex]
                    candidateAttributes = [chunk for chunk in chunked_sents[sIndex] if chunk[0][2]>hIndex]
                    entity = Entity(candidateEntityNames)
                    entity.setAttributes(candidateAttributes)
                    target.append(entity)
                    break


class PrimaryKeyExtractor(SecondaryExtractor):
    def execute(self, entities):
        pass


