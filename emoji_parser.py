from sentence_parser import SentenceParser


class EmojiParser(SentenceParser):
    def __init__(self):
        pass

    def parse(self, sentence):
        return sentence + '-Emoji_parsed'
