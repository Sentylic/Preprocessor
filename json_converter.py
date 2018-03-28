from abc import ABCMeta, abstractmethod
import json

class JsonConverter:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    @classmethod
    def _parse_post(cls, post_str):
        pass

    @classmethod
    def process(cls, post_file_path, output_file_path):
        parsed_posts = []
        with open(post_file_path, 'r') as tweet_file:
            for line in tweet_file:
                parsed_posts.append(cls._parse_post(line))
        with open(output_file_path, 'w') as output_file:
            output_file.write(json.dumps(parsed_posts.__dict__))

class TweetJsonConverter(JsonConverter):
    @classmethod
    def _parse_post(cls, post_str):
        pass

class TripAdvisorPostJsonConverter(JsonConverter):
    @classmethod
    def _parse_post(cls, post_str):
        pass
