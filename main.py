print("Vamos a calcular la raiz cuadrada")
numero = float(input("Ingrese el numero: "))
x = 1.0

for f in range(1,10):
    numero = (x + numero/x)/2
    print("la raiz cuadrade del numero es: ", numero)