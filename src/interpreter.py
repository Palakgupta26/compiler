import math
from src.my_ast import Number, BinOp, UnaryOp

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def factorial(n):
    if n < 0:
        raise RuntimeError("Factorial of negative number")
    if n == 0:
        return 1
    return n * factorial(n - 1)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

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
        elif ast.op == 'AREARECTANGLE':
            return left * right
        elif ast.op == 'PERIMETERRECTANGLE':
            return 2 * (left + right)
        elif ast.op == 'AREATRIANGLE':
            return 0.5 * left * right
        elif ast.op == 'AREAPARALLELOGRAM':
            return left * right
        elif ast.op == 'PERIMETERPARALLELOGRAM':
            return 2 * (left + right)
        elif ast.op == 'AREAELLIPSE':
            return math.pi * left * right
        elif ast.op == 'GCD':
            return gcd(left, right)
        elif ast.op == 'LCM':
            return lcm(left, right)
        elif ast.op == 'AVERAGE':
            return (left + right) / 2
        elif ast.op == 'MAXOFTWO':
            return max(left, right)
        elif ast.op == 'MINOFTWO':
            return min(left, right)
        elif ast.op == 'PERCENTAGE':
            return (right / left) * 100
        elif ast.op == 'REMAINDER':
            return left % right
        elif ast.op == 'SURFACEAREACYLINDER':
            return 2 * math.pi * left * right + 2 * math.pi * (left ** 2)
        elif ast.op == 'AREATRAPEZOID_ARG1':
            return left
        elif ast.op == 'AREATRAPEZOID_ARG2':
            base1 = interpret(ast.left.left)
            base2 = right
            height = left
            return 0.5 * (base1 + base2) * height
        elif ast.op == 'VOLUMECUBOID_ARG1':
            return left
        elif ast.op == 'VOLUMECUBOID_ARG2':
            return left * right * interpret(ast.left.right)
        elif ast.op == 'SURFACEAREACUBOID_ARG1':
            return left
        elif ast.op == 'SURFACEAREACUBOID_ARG2':
            l = interpret(ast.left.left)
            w = left
            h = right
            return 2 * (l*w + l*h + w*h)
        elif ast.op == 'VOLUMECONE_ARG1':
            return left
        elif ast.op == 'VOLUMECONE_ARG2':
            radius = interpret(ast.left.left)
            height = left
            return (1/3) * math.pi * (radius ** 2) * height
        elif ast.op == 'PERIMETERTRIANGLE_ARG1':
            return left
        elif ast.op == 'PERIMETERTRIANGLE_ARG2':
            side1 = interpret(ast.left.left)
            side2 = left
            side3 = right
            return side1 + side2 + side3
            
    elif isinstance(ast, UnaryOp):
        operand = interpret(ast.operand)
        if ast.op == 'ISEVEN':
            return operand % 2 == 0
        elif ast.op == 'ISODD':
            return operand % 2 != 0
        elif ast.op == 'SQRT':
            if operand < 0:
                raise RuntimeError("Square root of negative number")
            return math.sqrt(operand)
        elif ast.op == 'AREACIRCLE':
            return math.pi * (operand ** 2)
        elif ast.op == 'CIRCUMFERENCECIRCLE':
            return 2 * math.pi * operand
        elif ast.op == 'AREASQUARE':
            return operand ** 2
        elif ast.op == 'PERIMETERSQUARE':
            return 4 * operand
        elif ast.op == 'VOLUMECUBE':
            return operand ** 3
        elif ast.op == 'SURFACEAREACUBE':
            return 6 * (operand ** 2)
        elif ast.op == 'VOLUMESPHERE':
            return (4/3) * math.pi * (operand ** 3)
        elif ast.op == 'SURFACEAREASPHERE':
            return 4 * math.pi * (operand ** 2)
        elif ast.op == 'FACTORIAL':
            return factorial(operand)
        elif ast.op == 'ISPRIME':
            return is_prime(operand)
        elif ast.op == 'TORADIAN':
            return math.radians(operand)
        elif ast.op == 'TODEGREE':
            return math.degrees(operand)
        elif ast.op == 'TOFAHRENHEIT':
            return (operand * 9/5) + 32
        elif ast.op == 'TOCELSIUS':
            return (operand - 32) * 5/9
        elif ast.op == 'TOMILE':
            return operand * 0.621371
        elif ast.op == 'TOKM':
            return operand * 1.60934
        elif ast.op == 'TOHOUR':
            return operand / 60
        elif ast.op == 'TOMINUTE':
            return operand * 60
        elif ast.op == 'TOSECOND':
            return operand * 60
        elif ast.op == 'ABSOLUTE':
            return abs(operand)
        elif ast.op == 'RETURN':
            return operand
    else:
        raise RuntimeError(f"Unknown AST node: {type(ast)}")