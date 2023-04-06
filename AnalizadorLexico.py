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
        self._terminales = {    # Símbolos terminales, de entrada que acepta el autómata
            "digitos": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            "operadores": ["+", "-", "*", "/"],
        }
        self._pila = []
        self._listaTokens   # Lista de tokens a devolver al final

    def crearToken(
        value, tipo
    ):  # Formato de los tokens, integrarlo en la función de transición
        return {"valor": value, "tipo": tipo}

    def funcionTransicion(self, simboloEntrada):
        estado = self._estadoActual
        pila = self._pila
        topePila = pila[-1:]
        simbolosTerminales = self._terminales
        numeroSintetizado
        if estado == "Q0":  # Estado inicial
            if simboloEntrada in self.terminales["digitos"]:  # La entrada es un numero.
                estado = "Q1"
                numeroSintetizado = (
                    numeroSintetizado + simboloEntrada
                )  # Concatena el digito al numero.


# TODO: Planteamiento formal del autómata
