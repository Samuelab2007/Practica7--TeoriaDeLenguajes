# Idea: TODO: Al realizar el Parseo(construir el árbol), es necesario que al evaluar se pueda extraer cuál es la operación a realizar


class Node:
    def evaluate(self):
        pass


class BinOp(
    Node
):  # Nodo usado para representar expresiones y operaciones en el árbol sintáctico.
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def evaluate(
        self,
    ):  # Retorna el valor de la operación de manera recursiva. En caso de que BinOp apunte a otro BinOp.
        leftterm = self.left.evaluate()
        rightterm = self.right.evaluate()
        if self.op == "+":
            return float(leftterm + rightterm)
        elif self.op == "-":
            return float(leftterm - rightterm)
        elif self.op == "*":
            return float(leftterm * rightterm)
        elif self.op == "/":
            return float(leftterm / rightterm)
        # Recorre el arbol, o subarbol y se realiza las operaciones que representa.


class Number(Node):  # Nodo sencillo con el valor numérico de un token
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value


class Parser:  # Construye un arbol sintáctico, la raiz es una operación. Árbol INORDEN
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        return self.parse_expression()

    def parse_expression(self):
        left = self.parse_term()
        while self.pos < len(self.tokens) and self.tokens[self.pos] in ["+", "-"]:
            op = self.tokens[self.pos]  # Guarda el símbolo de la operación
            self.pos += 1  # Avanza a el otro término de la operación.
            right = self.parse_term()  # Lado derecho de la operación.
            left = BinOp(
                left, op, right
            )  # Crea un nodo BinOp, con la info del lado izquierdo(ya parseado), la operación y el lado derecho(no parseado)
        return left

    def parse_term(self):
        left = self.parse_factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos] in ["*", "/"]:
            op = self.tokens[self.pos]
            self.pos += 1
            right = self.parse_factor()
            left = BinOp(left, op, right)
        return left

    def parse_factor(self):  # Para los factores que componen un término
        if (
            self.tokens[self.pos] == "("
        ):  # Disminuye la ambiguedad agrupando con paréntesis
            self.pos += 1
            node = (
                self.parse_expression()
            )  # Parsea la expresión al interior del paréntesis. Y guarda la referencia al subárbol que la representa
            self.pos += 1
            return node
        else:  # Si no hay paréntesis
            node = Number(
                float(self.tokens[self.pos])
            )  # Crea un nodo Number con la información del número que representa el token
            self.pos += 1
            return node


tokens = ["(", "3", "+", "10", "-", "9", ")", "*", "(", "7", "-", "3", ")"]
parser = Parser(tokens)
tree = parser.parse()
print(tree.evaluate())  # Resultado de la operación

# Imprime 35
