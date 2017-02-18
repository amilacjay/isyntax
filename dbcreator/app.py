from dbcreator.core import *
from dbcreator.models import *
from dbcreator.extractors import *


class App:

    def __init__(self, filePath):
        self.filePath = filePath


    def run(self):

        text = getContentFromFile(self.filePath)

        entityList = []

        ## primary data sets
        tagged_sentences = getTaggedSentences(text)
        chunked_sents = getChunkedSentences(tagged_sentences)

        ## extractors List in the order of execution
        extractorsList = [PossessionBasedExtractor, PrimaryKeyExtractor]

        for extractor in extractorsList:
            extObject = extractor()

            if isinstance(extObject, PrimaryExtractor):
                extObject.execute(tagged_sents=tagged_sentences, target=entityList)

            elif isinstance(extObject, SecondaryExtractor):
                extObject.execute(entities=entityList)

        return entityList

## Main Program Executing


app = App(filePath='samples/sample1.txt')
entities = app.run()