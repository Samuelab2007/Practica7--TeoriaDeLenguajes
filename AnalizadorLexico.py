# Herramienta formal: Autómata.

# Entrada: Operación de la calculadora. Ej: 2+3*5
# Procesamiento: Recorre la entrada de la calculadora, cambiando de estados,
# verificando la validez dependiendo del estado y la entrada, y a cada paso se genera la lista de tokens.
# Salida: Verificación léxica y lista de tokens (token, tipo)


class AnalizadorLexico:
    def __init__(self, cadena):
        self._cadena = cadena
        self._valorNumero = (
            str()
        )  # Valor construido para el token numérico a generar, cambia dependiendo de las entradas
        self._operadores = ["+", "-", "*", "/"]
        self._digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self._listaTokens = []  # Lista de tokens a devolver al final

    def getListaTokens(self):
        return self._listaTokens

    def getValorNumero(self):
        return self._valorNumero

    def resetValorNumero(self):
        self._valorNumero = str()

    def crearToken(self, value, tipo):
        tokenCreado = {"tipo": tipo, "valor": value}
        self._listaTokens.append(tokenCreado)

    def generarTokens(self):
        for caracter in self._cadena:
            self.determinacionToken(caracter)
        if self.getValorNumero() != str():
            self.crearToken(
                self.getValorNumero(), "INTEGER"
            )  # Cuando se agota la cadena y estaba leyendo un numero

    def determinacionToken(self, simboloEntrada: str):  # Crea el token de caracter
        if simboloEntrada in self._digitos:  # La entrada es un numero.
            self._valorNumero += simboloEntrada
        elif simboloEntrada == "(":
            if self.getValorNumero() != str():
                self.crearToken(self._valorNumero, "INTEGER")
                self.resetValorNumero()
            self.crearToken(simboloEntrada, "PARENTESIS_IZQUIERDO")
        elif simboloEntrada == ")":
            if self.getValorNumero() != str():
                self.crearToken(self._valorNumero, "INTEGER")
                self.resetValorNumero()
            self.crearToken(simboloEntrada, "PARENTESIS_DERECHO")
        elif simboloEntrada in self._operadores:  # La entrada es un operador básico
            if self.getValorNumero() != str():
                self.crearToken(self._valorNumero, "INTEGER")
                self.resetValorNumero()
            if simboloEntrada == "+":
                self.crearToken(simboloEntrada, "OPERADOR_SUMA")
            elif simboloEntrada == "-":
                self.crearToken(simboloEntrada, "OPERADOR_RESTA")
            elif simboloEntrada == "*":
                self.crearToken(simboloEntrada, "OPERADOR_MULTIPLICACION")
            elif simboloEntrada == "/":
                self.crearToken(simboloEntrada, "OPERADOR_DIVISION")
        else:
            raise ValueError(
                "Error sintactico, la entrada no es un numero, operador, o parentesis"
            )
