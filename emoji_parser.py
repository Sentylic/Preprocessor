from sentence_parser import SentenceParser
import re
import emoji

class EmojiParser(SentenceParser):
    def __init__(self):
        pass

    def parse(self, sentence):
        return emoji.demojize(sentence)
