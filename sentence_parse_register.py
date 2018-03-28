from sentence_parser import SentenceParser


class SentenceParseRegister:
    def __init__(self):
        self.parsers = []

    def register(self, sentence_parser):
        assert isinstance(sentence_parser, SentenceParser)
        self.parsers.append(sentence_parser)
        return self
