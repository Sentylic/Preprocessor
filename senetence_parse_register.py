from sentence_parser import SentenceParser


class SentenceParseRegister:
    def __init__(self):
        self.parsers = [];

    def register(self, senetence_parser):
        assert isinstance(senetence_parser, SentenceParser)
        self.parsers.append(senetence_parser)
        return self
