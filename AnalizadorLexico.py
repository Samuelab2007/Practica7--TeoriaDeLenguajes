# Herramienta formal: Autómata.

# Entrada: Operación de la calculadora. Ej: 2+3*5
# Procesamiento: Recorre la entrada de la calculadora, cambiando de estados,
# verificando la validez dependiendo del estado y la entrada, y a cada paso se genera la lista de tokens.
# Salida: Verificación léxica y lista de tokens (token, tipo)


class AnalizadorLexico:
    def __init__(self, cadena):
        self._cadena = cadena
        self._listaEstados = ["Q0", "Q1"]
        self._estadoActual = "Q0"
        self._terminales = {  # Símbolos terminales, de entrada que acepta el autómata
            "digitos": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
            "operadores": ["+", "-", "*", "/"],
        }
        self._pila = []
        self._valorNumero = ""  # Valor construido para el token a generar, cambia con cada operacion en el autómata.
        self._recibeOperador = False
        self._listaTokens = []  # Lista de tokens a devolver al final

    def getListaTokens(self):
        return self._listaTokens

    def getValorNumero(self):
        return self._valorNumero

    def resetValorNumero(self):
        self._valorNumero = ""

    def crearToken(self, value, tipo):
        tokenCreado = {"tipo": tipo, "valor": value}
        self._listaTokens.append(tokenCreado)

    def transicionDigito(self, simboloEntrada: str):  # Concatena el digito y pasa a Q1
        self._estadoActual = "Q1"
        self._valorNumero += simboloEntrada  # Concatena el digito al numero.

    def transicionDos(self, simboloEntrada: str):
        self._estadoActual = "Q2"
        self._pila.append(simboloEntrada)
        tipoOperador = ""
        if simboloEntrada == "+":  # Determina el tipo de operador
            tipoOperador = "OPERADOR_SUMA"
        elif simboloEntrada == "-":
            tipoOperador = "OPERADOR_RESTA"
        elif simboloEntrada == "*":
            tipoOperador = "OPERADOR_MULTIPLICACION"
        elif simboloEntrada == "/":
            tipoOperador = "OPERADOR_DIVISION"
        self.crearToken(
            simboloEntrada, tipoOperador
        )  # Crea el token y lo guarda en la lista de tokens

    def transicionTres(self, simboloEntrada: str):
        self._estadoActual = "Q2"
        self._pila.pop()
        self._pila.append(simboloEntrada)
        self.crearToken(simboloEntrada, "PARENTESIS_IZQUIERDO")

    def transicionCuatro(self, simboloEntrada: str):
        self._estadoActual = "Q2"  # Transición cuatro
        self._recibeOperador = (
            True  # Para permitir operadores inmediatamante despues de parentesis.
        )
        self._pila.pop()
        self.crearToken(simboloEntrada, "PARENTESIS_DERECHO")

    def transicionCinco(self, simboloEntrada):
        self._estadoActual = "Q1"
        self._valorNumero += simboloEntrada
        self._pila.pop()

    def determinaraceptacion(self):
        if self._cadena[-1:] in self._terminales["operadores"]:
            return "Cadena Inválida"
        for caracter in self._cadena:
            aceptacioncaracter = self.funcionTransicion(caracter)
            if aceptacioncaracter == 99:
                return "Cadena Inválida"
        if self.getValorNumero() != "":
            self.crearToken(
                self.getValorNumero(), "INTEGER"
            )  # Cuando se agota la cadena y estaba leyendo un numero
        if len(self._pila) == 0:
            return "Cadena Válida"
        else:
            return "Cadena Inválida"

    def funcionTransicion(self, simboloEntrada: str):
        estado = self._estadoActual
        pila = self._pila
        topePila = pila[-1:]
        simbolosTerminales = self._terminales
        if estado == "Q0":  # Función de transición para Q0, Estado inicial
            if (
                simboloEntrada in simbolosTerminales["digitos"]
            ):  # La entrada es un numero.
                self.transicionDigito(simboloEntrada)
            elif simboloEntrada == "(":
                self.crearToken(simboloEntrada, "PARENTESIS_IZQUIERDO")
                estado = "Q2"
                pila.append(simboloEntrada)
            else:
                return 99
        elif estado == "Q1":  # Función de transición para Q1
            if len(pila) == 0:
                if simboloEntrada in simbolosTerminales["digitos"]:
                    self.transicionDigito(simboloEntrada)  # Transición Uno
                elif simboloEntrada in simbolosTerminales["operadores"]:
                    self.crearToken(
                        self.getValorNumero(), "INTEGER"
                    )  # Token con el numero anterior
                    self.resetValorNumero()  # Borro los digitos ya leídos
                    self.transicionDos(simboloEntrada)  # Transición Dos
                else:
                    return 99
            elif topePila[0] == "(":
                if simboloEntrada in simbolosTerminales["digitos"]:
                    self.transicionDigito(simboloEntrada)
                elif simboloEntrada in simbolosTerminales["operadores"]:
                    self.crearToken(
                        self.getValorNumero(), "INTEGER"
                    )  # Crea token con el numero anterior
                    self.resetValorNumero()  # Resetea el numero almacenado
                    self.transicionDos(simboloEntrada)
                elif simboloEntrada == ")":
                    self.crearToken(self.getValorNumero(), "INTEGER")
                    self.resetValorNumero()
                    self.transicionCuatro(simboloEntrada)
                else:
                    return 99
        elif estado == "Q2":  # Función de transición para Q2
            if len(pila) == 0:
                if simboloEntrada in simbolosTerminales["operadores"]:
                    self.transicionDos(simboloEntrada)
                else:
                    return 99
            elif topePila[0] in simbolosTerminales["operadores"]:
                if simboloEntrada in simbolosTerminales["digitos"]:
                    self.transicionCinco(simboloEntrada)
                elif simboloEntrada == "(":
                    self.transicionTres(simboloEntrada)
                else:
                    return 99
            elif topePila[0] == "(":
                if simboloEntrada in simbolosTerminales["digitos"]:
                    self.transicionDigito(simboloEntrada)
                elif (
                    simboloEntrada in simbolosTerminales["operadores"]
                    and self._recibeOperador == True
                ):
                    self.transicionDos(simboloEntrada)
                elif simboloEntrada == "(":
                    self.transicionDos(simboloEntrada)
                elif simboloEntrada == ")":
                    self.transicionCuatro(simboloEntrada)
                else:
                    return 99
