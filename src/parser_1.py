from src.my_ast import Number, BinOp, UnaryOp

def parse_term(tokens):
    if not tokens:
        raise RuntimeError("Unexpected end of input")
    token = tokens.pop(0)
    if token[0] == 'NUMBER':
        return Number(token[1])
    else:
        raise RuntimeError(f"Unexpected token: {token[0]}")

def parse(tokens):
    tokens = list(tokens) 

    if len(tokens) < 4:
        raise RuntimeError("Invalid expression. Expected format: <function>(<arguments>)")

    func_token = tokens.pop(0)
    valid_ops = [
        'ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MOD', 'POWER', 
        'ISEVEN', 'ISODD', 'SQRT', 'AREACIRCLE', 'CIRCUMFERENCECIRCLE',
        'AREARECTANGLE', 'PERIMETERRECTANGLE', 'AREASQUARE', 
        'PERIMETERSQUARE', 'AREATRIANGLE', 'PERIMETERTRIANGLE',
        'AREATRAPEZOID', 'AREAPARALLELOGRAM', 'PERIMETERPARALLELOGRAM',
        'AREAELLIPSE', 'VOLUMECUBE', 'SURFACEAREACUBE', 'VOLUMESPHERE',
        'SURFACEAREASPHERE', 'VOLUMECUBOID', 'SURFACEAREACUBOID',
        'VOLUMECONE', 'SURFACEAREACYLINDER', 'FACTORIAL', 'ISPRIME',
        'GCD', 'LCM', 'AVERAGE', 'TORADIAN', 'TODEGREE', 'TOFAHRENHEIT',
        'TOCELSIUS', 'TOMILE', 'TOKM', 'TOHOUR', 'TOMINUTE', 'TOSECOND',
        'MAXOFTWO', 'MINOFTWO', 'PERCENTAGE', 'ABSOLUTE', 'REMAINDER',
        'RETURN'
    ]
    
    if func_token[0] not in valid_ops:
        raise RuntimeError(f"Invalid function: {func_token[1]}")

    lparen_token = tokens.pop(0)
    if lparen_token[0] != 'LPAREN':
        raise RuntimeError(f"Expected '(', found: {lparen_token[1]}")

    left = parse_term(tokens)

    # Unary operations
    unary_ops = [
        'ISEVEN', 'ISODD', 'SQRT', 'AREACIRCLE', 'CIRCUMFERENCECIRCLE',
        'AREASQUARE', 'PERIMETERSQUARE', 'VOLUMECUBE', 'SURFACEAREACUBE',
        'VOLUMESPHERE', 'SURFACEAREASPHERE', 'FACTORIAL', 'ISPRIME',
        'TORADIAN', 'TODEGREE', 'TOFAHRENHEIT', 'TOCELSIUS', 'TOMILE',
        'TOKM', 'TOHOUR', 'TOMINUTE', 'TOSECOND', 'ABSOLUTE', 'RETURN'
    ]
    if func_token[0] in unary_ops:
        rparen_token = tokens.pop(0)
        if rparen_token[0] != 'RPAREN':
            raise RuntimeError(f"Expected ')', found: {rparen_token[1]}")
        if tokens: 
            raise RuntimeError("Unexpected tokens after expression")
        return UnaryOp(left, func_token[0])
    
    # Binary operations
    binary_ops = [
        'AREARECTANGLE', 'PERIMETERRECTANGLE', 'AREATRIANGLE',
        'AREAPARALLELOGRAM', 'PERIMETERPARALLELOGRAM', 'AREAELLIPSE',
        'GCD', 'LCM', 'AVERAGE', 'MAXOFTWO', 'MINOFTWO', 'PERCENTAGE',
        'REMAINDER', 'SURFACEAREACYLINDER'
    ]
    if func_token[0] in binary_ops:
        if len(tokens) < 3:
            raise RuntimeError("Expected binary operation with two arguments")
        
        comma_token = tokens.pop(0)
        if comma_token[0] != 'COMMA':
            raise RuntimeError(f"Expected ',', found: {comma_token[1]}")

        right = parse_term(tokens)

        rparen_token = tokens.pop(0)
        if rparen_token[0] != 'RPAREN':
            raise RuntimeError(f"Expected ')', found: {rparen_token[1]}")
        
        if tokens:  
            raise RuntimeError("Unexpected tokens after expression")

        return BinOp(left, func_token[0], right)
    
    # Ternary operations
    ternary_ops = ['AREATRAPEZOID', 'VOLUMECUBOID', 'SURFACEAREACUBOID', 'VOLUMECONE']
    if func_token[0] in ternary_ops:
        if len(tokens) < 5:
            raise RuntimeError(f"Expected three arguments for {func_token[1]}")
        
        comma1 = tokens.pop(0)
        if comma1[0] != 'COMMA':
            raise RuntimeError(f"Expected ',', found: {comma1[1]}")
        
        middle = parse_term(tokens)
        
        comma2 = tokens.pop(0)
        if comma2[0] != 'COMMA':
            raise RuntimeError(f"Expected ',', found: {comma2[1]}")
        
        right = parse_term(tokens)
        
        rparen_token = tokens.pop(0)
        if rparen_token[0] != 'RPAREN':
            raise RuntimeError(f"Expected ')', found: {rparen_token[1]}")
        
        if tokens:
            raise RuntimeError("Unexpected tokens after expression")
        
        return BinOp(BinOp(left, f'{func_token[0]}_ARG1', middle), f'{func_token[0]}_ARG2', right)
    
    # Default binary operations
    if len(tokens) < 3:
        raise RuntimeError("Expected binary operation with two arguments")
    
    comma_token = tokens.pop(0)
    if comma_token[0] != 'COMMA':
        raise RuntimeError(f"Expected ',', found: {comma_token[1]}")

    right = parse_term(tokens)

    rparen_token = tokens.pop(0)
    if rparen_token[0] != 'RPAREN':
        raise RuntimeError(f"Expected ')', found: {rparen_token[1]}")
    
    if tokens:  
        raise RuntimeError("Unexpected tokens after expression")

    return BinOp(left, func_token[0], right)