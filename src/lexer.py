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
        ('SQRT', r'sqrt'),
        ('ISEVEN', r'iseven'),
        ('ISODD', r'isodd'),
        ('ISPRIME', r'isPrime'),
        ('FACTORIAL', r'factorial'),
        ('GCD', r'gcd'),
        ('LCM', r'lcm'),
        ('AVERAGE', r'average'),
        ('MAXOFTWO', r'maxOfTwo'),
        ('MINOFTWO', r'minOfTwo'),
        ('ABSOLUTE', r'absolute'),
        ('REMAINDER', r'remainder'),
        ('RETURN', r'return'),
        ('PERCENTAGE', r'percentage'),
        ('TORADIAN', r'toRadian'),
        ('TODEGREE', r'toDegree'),
        ('TOFAHRENHEIT', r'toFahrenheit'),
        ('TOCELSIUS', r'toCelsius'),
        ('TOMILE', r'toMile'),
        ('TOKM', r'toKm'),
        ('TOHOUR', r'toHour'),
        ('TOMINUTE', r'toMinute'),
        ('TOSECOND', r'toSecond'),
        ('AREACIRCLE', r'areaCircle'),
        ('CIRCUMFERENCECIRCLE', r'circumferenceCircle'),
        ('AREARECTANGLE', r'areaRectangle'),
        ('PERIMETERRECTANGLE', r'perimeterRectangle'),
        ('AREASQUARE', r'areaSquare'),
        ('PERIMETERSQUARE', r'perimeterSquare'),
        ('AREATRIANGLE', r'areaTriangle'),
        ('PERIMETERTRIANGLE', r'perimeterTriangle'),
        ('AREATRAPEZOID', r'areaTrapezoid'),
        ('AREAPARALLELOGRAM', r'areaParallelogram'),
        ('PERIMETERPARALLELOGRAM', r'perimeterParallelogram'),
        ('AREAELLIPSE', r'areaEllipse'),
        ('VOLUMECUBE', r'volumeCube'),
        ('SURFACEAREACUBE', r'surfaceAreaCube'),
        ('VOLUMESPHERE', r'volumeSphere'),
        ('SURFACEAREASPHERE', r'surfaceAreaSphere'),
        ('VOLUMECUBOID', r'volumeCuboid'),
        ('SURFACEAREACUBOID', r'surfaceAreaCuboid'),
        ('VOLUMECONE', r'volumeCone'),
        ('SURFACEAREACYLINDER', r'surfaceAreaCylinder'),
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