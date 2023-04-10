# Analizador sintáctico descendente recursivo, que utiliza una gramática libre de contexto atribuida.

# Entrada: Tokens con el tipo de token
# Procesamiento: Intenta generar la lista de tokens usando las reglas gramaticales.
# Cada regla de producción se implementa mediante un método en la clase AnalizadorSintactico
# Salida: Validez sintáctica y el resultado de la operación

# Reglas de producción
# <expr> --> <term> | <term>+<expr> | <term>-<expr>
# <term> --> <factor> | <factor>*<term> | <factor>/<term>
# <factor> --> <num> | (<expr>)         <num> puede expresar cualquier número entero positivo.


class AnalizadorSintactico:
    def __init__(self, listaToken: list):
        self._listaTokenEntrada = listaToken
        self.pos = 0
        self._simboloInicial = "<expr>"

    def getListaTokens(self):
        return self._listaTokenEntrada

    def parse(self):
        resultado = self.expr()
        if self.pos != len(self.getListaTokens()):
            raise ValueError("Expresión inválida")
        else:
            return resultado

    def expr(
        self,
    ):  # Regla de producción "<expr>": ["<term>", "<term>+<expr>", "<term>-<expr>"]
        result = self.term()
        while self.pos < len(self.getListaTokens()):
            if self.getListaTokens()[self.pos]["tipo"] == "OPERADOR_SUMA":
                self.pos += 1
                result += float(self.term())
            elif self.getListaTokens()[self.pos]["tipo"] == "OPERADOR_RESTA":
                self.pos += 1
                result -= float(self.term())
            else:
                break
        return result

    def term(
        self,
    ):  # Regla de producción  "<term>": ["<factor>", "<factor>*<term>", "<factor>/<term>"]
        result = self.factor()
        while self.pos < len(self.getListaTokens()):
            if self.getListaTokens()[self.pos]["tipo"] == "OPERADOR_MULTIPLICACION":
                self.pos += 1
                result *= float(self.factor())
            elif self.getListaTokens()[self.pos]["tipo"] == "OPERADOR_DIVISION":
                self.pos += 1
                result /= float(self.factor())
            else:
                break
        return result

    def factor(self):  # Regla de producción "<factor>": ["<num>", "(<expr>)"],
        if self.getListaTokens()[self.pos]["tipo"] == "PARENTESIS_IZQUIERDO":
            self.pos += 1
            result = self.expr()
            if self.getListaTokens()[self.pos]["tipo"] == "PARENTESIS_DERECHO":
                self.pos += 1
                return result
            else:
                raise ValueError("Se esperaba )")
        elif (
            self.getListaTokens()[self.pos]["tipo"] == "INTEGER"
        ):  # Cuando el token representa un numero
            result = float(self.getListaTokens()[self.pos]["valor"])
            self.pos += 1
            return result
        else:
            raise ValueError("Se esperaba un numero entero positivo")
