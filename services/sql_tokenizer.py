import re

class SQLTokenizer:
    # Single regex pattern matching SQL token groups
    _REGEX = re.compile(
        r"(?P<COMMENT>--[^\n]*|\/\*[\s\S]*?\*\/)|"
        r"(?P<STRING>'[^']*'|\"[^\"]*\")|"
        r"(?P<KEYWORD>\b(?:SELECT|FROM|WHERE|JOIN|LEFT|RIGHT|INNER|OUTER|CROSS|FULL|ON|INSERT|INTO|UPDATE|SET|DELETE|CREATE|TABLE|ALTER|DROP|TRUNCATE|REPLACE|GROUP|BY|ORDER|HAVING|UNION|ALL|INTERSECT|EXCEPT)\b)|"
        r"(?P<PAGINATION>\b(?:TOP|LIMIT|OFFSET|FETCH|FIRST|ROWS|ONLY)\b)|"
        r"(?P<CONTROL_FLOW>\b(?:CASE|WHEN|THEN|ELSE|END|IIF|CHOOSE|IF|WHILE)\b)|"
        r"(?P<FUNCTION>\b(?:CAST|CONVERT|COALESCE|NULLIF|ISNULL|NVL|CONCAT|SUBSTRING|COUNT|SUM|AVG|MIN|MAX|GETDATE|NOW|ROW_NUMBER|OVER|PARTITION)\b)|"
        r"(?P<LOGICAL>\b(?:AND|OR|NOT|NULL|AS|IN|BETWEEN|LIKE|ILIKE|EXISTS|IS|TRUE|FALSE|ANY|ALL|SOME)\b)|"
        r"(?P<NUMBER>\b\d+(?:\.\d+)?\b)|"
        r"(?P<OPERATOR><=|>=|!=|<>|=|<|>|\+|\-|\*|\/)",
        re.IGNORECASE
    )

    @classmethod
    def get_line_tokens(cls, line_text: str):
        
        for match in cls._REGEX.finditer(line_text):
            token_type = match.lastgroup
            yield token_type, match.start(), match.end()