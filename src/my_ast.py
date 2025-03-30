class ASTNode:
    pass

class Number(ASTNode):
    def __init__(self, value):
        self.value = value

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class UnaryOp(ASTNode):
    def __init__(self, operand, op):
        self.operand = operand
        self.op = op