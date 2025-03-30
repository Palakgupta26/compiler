from src.my_ast import Number, BinOp, UnaryOp

def parse(tokens):
    tokens = list(tokens) 

    if len(tokens) < 4:
        raise RuntimeError("Invalid expression. Expected format: <function>(<arguments>)")

    func_token = tokens.pop(0)
    if func_token[0] not in ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MOD', 'POWER', 'ISEVEN', 'ISODD'):
        raise RuntimeError(f"Invalid function: {func_token[1]}")

    lparen_token = tokens.pop(0)
    if lparen_token[0] != 'LPAREN':
        raise RuntimeError(f"Expected '(', found: {lparen_token[1]}")

    left = parse_term(tokens)

    if func_token[0] in ('ISEVEN', 'ISODD'):

        rparen_token = tokens.pop(0)
        if rparen_token[0] != 'RPAREN':
            raise RuntimeError(f"Expected ')', found: {rparen_token[1]}")
        if tokens: 
            raise RuntimeError("Unexpected tokens after expression")
        return UnaryOp(left, func_token[0])
    else:
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

def parse_term(tokens):
    if not tokens:
        raise RuntimeError("Unexpected end of input")
    token = tokens.pop(0)
    if token[0] == 'NUMBER':
        return Number(token[1])
    else:
        raise RuntimeError(f"Unexpected token: {token[0]}")