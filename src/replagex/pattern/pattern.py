
class Pattern:
    regex: str = ''
    replace: str = ''
    dotall: bool = False

    def __init__(self, regex: str, replace: str, dotall: bool = False):
        self.regex = str(regex)
        self.replace = str(replace).replace("$", "\\")
        self.dotall = dotall
