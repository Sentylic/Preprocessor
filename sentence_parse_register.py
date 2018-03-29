import os
import json
from sentence_parser import SentenceParser


class SentenceParseRegister:
	def __init__(self):
		self.parsers = []

	def register(self, sentence_parser):
		assert isinstance(sentence_parser, SentenceParser)
		self.parsers.append(sentence_parser)
		return self

	def process(self, input_dir, output_dir):
		for filename in os.listdir(input_dir):
			if filename.endswith(".json"):
				outputFilename = output_dir + "/output-" + filename
				outputArray = []
				file = json.load(open(input_dir + "/" + filename))
				for data in file:
					parsedData = data["content"]
					for parser in self.parsers:
						parsedData = parser.parse(parsedData)
						data["content"] = parsedData
					outputArray.append(data)
				with open(outputFilename, 'wb') as outfile:
					json.dump(outputArray, outfile)
			else:
				continue

