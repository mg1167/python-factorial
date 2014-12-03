#******************************************************************************
#*************************** FACTORIAL ****************************************
print "*** FACTORIAL ***"
print "Calculo del factorial de el numero que desee."
numero =input("Ingrese el numero que desee: ")
def factorial(numero):
    if numero == 1:
        return 1
    else:
        respuesta = numero * factorial(numero-1)
        return respuesta
print"El calculo del factorial de %s es: "%(numero)
print(factorial(numero))
