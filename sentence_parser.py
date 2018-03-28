from abc import ABCMeta, abstractmethod


class SentenceParser:
    def __init__(self):
        pass

    __metaclass__ = ABCMeta

    @abstractmethod
    def parse(self, sentence):
        pass
