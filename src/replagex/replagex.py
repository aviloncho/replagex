import re
import json

from .pattern import Pattern


class Replagex:

    def __init__(self, json_file=None):
        self.patterns: list = []

        if json_file:
            self.load_from_json_file(json_file)

    def load_from_json_file(self, file):
        with open(file, 'r') as f:
            try:
                data = json.load(f)
            except Exception as e:
                raise Exception(f'Failed to load JSON file "{file}": ' +
                                str(e))

        for patt in data['patterns']:
            if not ('regex' in patt.keys()):
                continue

            self.patterns.append(
                Pattern(
                    patt['regex'],
                    patt.get('replace', ''),
                    patt.get('dotall', False),
                    patt.get('ignore_case', False),
                    patt.get('multiline', False)
                )
            )

    def add_pattern(self, pattern):
        if isinstance(pattern, Pattern):
            self.patterns.append(pattern)
        else:
            raise Exception("The pattern sent is not a Pattern instance.")

    def apply_regex(self, text):
        result = text
        if not self.patterns:
            return result

        for patt in self.patterns:
            regex = re.compile(patt.regex, flags=patt.flags())

            try:
                result = regex.sub(patt.replace, result)
            except Exception as e:
                raise Exception(f'Failed to replace "{patt.replace}" ' +
                                f'on regex "{patt.regex}": ' + str(e))

        return result
