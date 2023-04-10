import AnalizadorLexico as AL
import AnalizadorSintactico as AS


operacion = input("Ingrese una operación simple: ")
Lexer = AL.AnalizadorLexico(operacion)
Lexer.generarTokens()
tokens = Lexer.getListaTokens()

print("Estos son los tokens generados por el analizador léxico ")
print(tokens)
print(
    "Este es el resultado del análisis sintáctico de los tokens(si retorna un número, es una cadena válida)"
)
try:
    Parser = AS.AnalizadorSintactico(tokens)
    print(Parser.parse())
except ZeroDivisionError:
    print("Math Error, división entre cero")
except Exception:
    print("Expresión Inválida")
