from sentence_parser import SentenceParser


class FrequentWordParser(SentenceParser):
	def __init__(self):
		pass

	def parse(self, sentence):
		return sentence + '-Frequent_word_parsed'
