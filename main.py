from emoji_parser import EmojiParser
from sentence_parse_register import SentenceParseRegister
from frequent_word_parser import FrequentWordParser

# sentence parser
emojiParser = EmojiParser()
frequentWordParser = FrequentWordParser()

# registration component
sentenceParseRegister = SentenceParseRegister()


sentenceParseRegister.register(emojiParser).register(frequentWordParser)

print sentenceParseRegister.parsers