import re


class Pattern:
    regex: str = ''
    replace: str = ''
    dotall: bool = False
    ignore_case: bool = False
    multiline: bool = False

    def __init__(self, regex: str, replace: str, dotall: bool = False,
                 ignore_case: bool = False, multiline: bool = False):
        self.regex = str(regex)
        self.replace = str(replace).replace("$", "\\")
        self.dotall = dotall
        self.ignore_case = ignore_case
        self.multiline = multiline

    def flags(self):
        flags = 0

        if self.dotall:
            flags += re.DOTALL
        if self.ignore_case:
            flags += re.IGNORECASE
        if self.multiline:
            flags += re.MULTILINE

        return flags
