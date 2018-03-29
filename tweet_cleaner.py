from sentence_parser import SentenceParser
import re

class TweetCleaner(SentenceParser):
	def __init__(self):
		pass
	
	@staticmethod
    def parse(self, sentence):
        text = sentence
		text = re.sub(r'http\S+', '', text)
		text = re.sub(r'\&\S+;', '', text)
		text = re.sub(r'\\u[0-9]+', '', text)
		text = re.sub(r'@\S+', '', text)
		text = re.sub(r'#', '',text)
		return text.strip()
