import re

class SQLTokenizer:
    # Single regex pattern matching SQL token groups
    _REGEX = re.compile(
        r"(?P<COMMENT>--[^\n]*|\/\*[\s\S]*?\*\/)|"
        r"(?P<STRING>'[^']*'|\"[^\"]*\")|"
        r"(?P<KEYWORD>\b(?:SELECT|FROM|WHERE|JOIN|LEFT|RIGHT|INNER|ON|INSERT|INTO|UPDATE|DELETE|GROUP|BY|ORDER|HAVING|LIMIT|AND|OR|NOT|NULL|AS)\b)|"
        r"(?P<NUMBER>\b\d+(?:\.\d+)?\b)|"
        r"(?P<OPERATOR><=|>=|!=|<>|=|<|>|\+|\-|\*|\/)",
        re.IGNORECASE
    )

    @classmethod
    def get_line_tokens(cls, line_text: str):
        """Yields (token_type, start_col, end_col) for non-whitespace matches on a single line."""
        for match in cls._REGEX.finditer(line_text):
            token_type = match.lastgroup
            yield token_type, match.start(), match.end()