# Herramienta formal: Gramática libre de contexto atribuida.

# Entrada: Tokens con el tipo de token
# Procesamiento: Intenta generar la lista de tokens usando la gramática y construye el árbol sintáctico.
# Salida: Validez sintáctica y el resultado de la operación (recorriendo el árbol)


alphabet = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "(", ")", "+", "-", "*", "/"]
variables = ["expr", "term", "factor", "digit"]


# TODO: Planteamiento formal de la gramática atribuida.
