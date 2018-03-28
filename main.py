from emoji_parser import EmojiParser
from senetence_parse_register import SentenceParseRegister
from frequent_word_parser import FrequentWordParser

# sentence parser
emojiParser = EmojiParser()
frequentWordParser = FrequentWordParser()

# registration component
sentenceParseRegister = SentenceParseRegister()


sentenceParseRegister.register(emojiParser)
sentenceParseRegister.register(frequentWordParser)

print sentenceParseRegister.parsers