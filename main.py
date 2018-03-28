from emoji_parser import EmojiParser
from sentence_parse_register import SentenceParseRegister
from frequent_word_parser import FrequentWordParser

# sentence parser
emojiParser = EmojiParser()
frequentWordParser = FrequentWordParser()

# registration component
sentenceParseRegister = SentenceParseRegister()

# register each sentence parser component
sentenceParseRegister\
    .register(emojiParser)\
    .register(frequentWordParser)

# process input files
sentenceParseRegister.process("Input", "Output")