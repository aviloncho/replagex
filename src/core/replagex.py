import re
import json

from .pattern import Pattern


class Replagex:
    patterns = []

    def __init__(self, file):
        self.load_from_json_file(file)

    def load_from_json_file(self, file):
        with open(file, 'r') as f:
            data = json.load(f)

        for patt in data['patterns']:
            self.patterns.append(
                Pattern(
                    patt['regex'],
                    patt['replace'],
                    patt.get('dotall', False)
                )
            )

    def apply_regex(self, text):
        result = text
        if not self.patterns:
            return result

        for patt in self.patterns:
            if patt.dotall:
                regex = re.compile(patt.regex, re.DOTALL)
            else:
                regex = re.compile(patt.regex)
            result = regex.sub(patt.replace, result)
        return result
