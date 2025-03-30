import re

def lex(input_string):
    tokens = []
    token_specification = [
        ('NUMBER', r'\d+'),  
        ('ADD', r'add'),
        ('SUBTRACT', r'subtract'),  
        ('MULTIPLY', r'multiply'), 
        ('DIVIDE', r'divide'),
        ('MOD', r'mod'),
        ('POWER', r'power'),
        ('ISEVEN', r'iseven'),
        ('ISODD', r'isodd'),    
        ('LPAREN', r'\('),
        ('RPAREN', r'\)'),
        ('COMMA', r','),
        ('SKIP', r'[ \t]'),
        ('MISMATCH', r'.'),
    ]
    token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
    for match in re.finditer(token_regex, input_string):
        kind = match.lastgroup
        value = match.group()
        if kind == 'NUMBER':
            value = int(value)
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character: {value}')
        tokens.append((kind, value))
    return tokens