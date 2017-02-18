class PrimaryExtractor:
    def execute(self, tagged_sents, target):
        pass


class SecondaryExtractor:
    def execute(self, entities):
        pass


class PossessionBasedExtractor(PrimaryExtractor):
    def execute(self, tagged_sents, target):
        # for word, tag in tagged_sents:
        #     if word == 'has' or word == 'have':
        #         pass
        print('Possession Based Extractor')
        pass


class PrimaryKeyExtractor(SecondaryExtractor):
    def execute(self, entities):
        print('Primary Key Extractor')


