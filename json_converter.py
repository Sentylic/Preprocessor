from abc import ABCMeta, abstractmethod
import json

class JsonConverter:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    @classmethod
    def _parse_post(cls, post_str):
        """
        Parse a social media post text to a dictionary object

        Args:
            post_str: social media post text string
        Returns:
            Parsed dictionary object
        """
        pass

    @classmethod
    def process(cls, post_file_path, output_file_path):
        """
        Process an input file containing social media posts line by line and converts them to
        a json array and writes to the specified output file

        Args:
            post_file_path: input file path
            param output_file_path: output json file path
        Raises:
            IOError: file reading or writing error
        """
        parsed_posts = []
        try:
            with open(post_file_path, 'r') as tweet_file:
                for line in tweet_file:
                    parsed_posts.append(cls._parse_post(line))
        except IOError:
            raise IOError('IOError while reading')
        try:
            with open(output_file_path, 'w') as output_file:
                output_file.write(json.dumps(parsed_posts))
        except IOError:
            raise IOError('IOError while writing')


class TweetJsonConverter(JsonConverter):
    @classmethod
    def _parse_post(cls, post_str):
        """
        Parses a Tweet post string to a dictionary object
        
        Args:
            post_str: tweet post text string
        Returns:
            Parsed dictionary object
        """
        pass

class TripAdvisorPostJsonConverter(JsonConverter):
    @classmethod
    def _parse_post(cls, post_str):
        """
        Parses a Trip Advisor post string to a dictionary object
        
        Args:
            post_str: Trip Advisor post text string
        Returns:
            Parsed dictionary object
        """
        pass

