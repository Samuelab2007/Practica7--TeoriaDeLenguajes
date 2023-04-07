# Herramienta formal: Autómata.

# Entrada: Operación de la calculadora. Ej: 2+3*5
# Procesamiento: Recorre la entrada de la calculadora, cambiando de estados,
# verificando la validez dependiendo del estado y la entrada, y a cada paso se genera la lista de tokens.
# Salida: Verificación léxica y lista de tokens (token, tipo)


def crearToken(
    value, tipo
):  # Formato de los tokens, integrarlo en la función de transición
    return {"valor": value, "tipo": tipo}


class AnalizadorLexico:
    def __init__(self, cadena):
        self._cadena = cadena
        self._listaEstados = ["Q0", "Q1"]
        self._estadoActual = "Q0"
        self._terminales = {  # Símbolos terminales, de entrada que acepta el autómata
            "digitos": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            "operadores": ["+", "-", "*", "/"],
        }
        self._pila = []
        self._valorToken = ""  # Valor construido para el token a generar, cambia con cada operacion en el autómata.
        self._listaTokens  # Lista de tokens a devolver al final

    def transicionDigito(self, simboloEntrada: str):  # Concatena el digito y pasa a Q1
        self._estadoActual = "Q1"
        self._valorToken += simboloEntrada  # Concatena el digito al numero.

    def transicionDos(self, simboloEntrada: str):
        self._estadoActual = "Q2"
        tipoOperador = ""
        if simboloEntrada == "+":  # Determina el tipo de operador
            tipoOperador = "OPERADOR_SUMA"
        elif simboloEntrada == "-":
            tipoOperador = "OPERADOR_RESTA"
        elif simboloEntrada == "*":
            tipoOperador = "OPERADOR_MULTIPLICACION"
        elif simboloEntrada == "/":
            tipoOperador = "OPERADOR_DIVISION"
        crearToken(
            simboloEntrada, tipoOperador
        )  # Crea el token y lo guarda en la lista de tokens

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
                estado = "Q2"
                pila.append(simboloEntrada)
            else:
                return 99
        if estado == "Q1":  # Función de transición para Q1
            if len(pila) == 0:
                if simboloEntrada in simbolosTerminales["digitos"]:
                    self.transicionDigito(simboloEntrada)  # Transición Uno
                elif simboloEntrada in simbolosTerminales["operadores"]:
                    self.transicionDos(simboloEntrada)  # Transición Dos
                else:
                    return 99
            elif topePila[0] == "(":
                if simboloEntrada in simbolosTerminales["digitos"]:
                    self.transicionDigito(simboloEntrada)
                elif simboloEntrada in simbolosTerminales["operadores"]:
                    self.transicionDos(simboloEntrada)
                elif simboloEntrada == ")":
                    estado = "Q2"  # Transición cuatro
                    pila.pop()
                else:
                    return 99


# TODO: Planteamiento formal del autómata
