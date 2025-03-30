from src.my_ast import Number, BinOp, UnaryOp

def interpret(ast):
    if isinstance(ast, Number):
        return ast.value
    elif isinstance(ast, BinOp):
        left = interpret(ast.left)
        right = interpret(ast.right)
        if ast.op == 'ADD':
            return left + right
        elif ast.op == 'SUBTRACT':
            return left - right
        elif ast.op == 'MULTIPLY':
            return left * right
        elif ast.op == 'DIVIDE':
            if right == 0:
                raise RuntimeError("Division by zero")
            return left / right
        elif ast.op == 'MOD':
            return left % right
        elif ast.op == 'POWER':
            return left ** right
    elif isinstance(ast, UnaryOp):
        operand = interpret(ast.operand)
        if ast.op == 'ISEVEN':
            return operand % 2 == 0
        elif ast.op == 'ISODD':
            return operand % 2 != 0
    else:
        raise RuntimeError(f"Unknown AST node: {type(ast)}")