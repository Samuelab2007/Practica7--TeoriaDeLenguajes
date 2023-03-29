class Node:
    def evaluate(self):
        pass

class BinOp(Node): # Estudiar como funciona este nodo, si guarda referencias o valores
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    def evaluate(self):
        pass # Recorre el arbol, o subarbol y se realiza las operaciones que representa.

class Number(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value

class Parser:   # Construye un arbol sintáctico, la raiz es una operación
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        return self.parse_expression()

    def parse_expression(self):
        left = self.parse_term()
        while self.pos < len(self.tokens) and self.tokens[self.pos] in ['+', '-']:
            op = self.tokens[self.pos]
            self.pos += 1
            right = self.parse_term()
            left = BinOp(left, op, right)
        return left

    def parse_term(self):
        left = self.parse_factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos] in ['*', '/']:
            op = self.tokens[self.pos]
            self.pos += 1
            right = self.parse_factor()
            left = BinOp(left, op, right)
        return left

    def parse_factor(self):
        if self.tokens[self.pos] == '(':
            self.pos += 1
            node = self.parse_expression()
            self.pos += 1
            return node
        else:
            node = Number(int(self.tokens[self.pos]))
            self.pos += 1
            return node


tokens = ['(', '3', '+', '4', ')', '*', '5']
parser = Parser(tokens)
tree = parser.parse()
# print(tree.evaluate())
print(tree.left.right.evaluate())
# Imprime 35
