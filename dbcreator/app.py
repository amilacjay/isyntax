from dbcreator.extractors import *


class App:

    def __init__(self, filePath):
        self.filePath = filePath


    def run(self):

        text = getContentFromFile(self.filePath)

        entityList = []

        ## primary data sets
        tagged_sentences = getTaggedSentences(text)
        chunked_sentences = getChunkedSentences(tagged_sentences)
        # print(chunked_sentences)

        ne_chunked_sentences = getNamedEntities(text)
        # re = extract_relations(tagged_sentences)

        ## extractors List in the order of execution
        extractorsList = [PossessionBasedExtractor, UniqueKeyExtractor, RemoveDuplicateEntities, RemoveDuplicateAttributes,
                          IdentifyAttributeDataType, RemoveNonPotentialEntities, SuggestRelationshipTypes] #, SuggestRelationshipTypes, FilterNPE

        for extractor in extractorsList:
            extObject = extractor()

            if isinstance(extObject, PrimaryExtractor):
                extObject.execute(tagged_sents=tagged_sentences, chunked_sents=chunked_sentences, ne_chunked_sents=ne_chunked_sentences, target=entityList)

            elif isinstance(extObject, SecondaryExtractor):
                extObject.execute(entities=entityList)

        for e in entityList:
            for r in e.relationships:
                print(r[0].name(), r[1].name())

        return entityList

## Main Program Executing

if __name__ == "__main__":
    app = App(filePath='samples/sample1.txt')
    entities = app.run()

    for i, e in enumerate(entities):
        print('Entity: ', e.name())
        print('Candidate Attributes', [x.name() for x in e.attributes])
        print()