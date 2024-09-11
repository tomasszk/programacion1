import random

def login():
    # Credenciales predefinidas
    usuarioCorrecto = "mozo"
    contraseñaCorrecta = "12345"
    print("Por favor, ingrese sus credenciales para acceder.")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    # Validar credenciales
    if usuario == usuarioCorrecto and contraseña == contraseñaCorrecta:
        print("Acceso permitido. Bienvenido.")
        return True
    else:
        print("Credenciales incorrectas.")
        return False
 
def obtenerSector():
    # Solicita al usuario el sector deseado y valida la entrada
    while True:
        sector = int(input("Ingrese 1 si quiere adentro, 2 si quiere afuera (o -1 para terminar carga): "))
        if sector in [1, 2]:
            return sector
        if sector == -1:
            return -1
        print("Sector inválido. Vuelva a ingresar el sector.")
 
def asignarMozo():
    # Asigna aleatoriamente uno de los dos mozos
    mozo = random.randint(1, 2)
    print(f"El mozo que atenderá es el mozo {mozo}")
    return mozo

def reseñaCliente():
    # Genera una reseña aleatoria del cliente
    reseña = random.randint(1, 5)
    print(f"La calificación del comensal es {reseña}")
    return reseña
 
def imprimirMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%20s" % str(matriz[f][c]), end=" ")  # Formato para alinear y mostrar bien los datos
        print()

calcularComision = lambda monto: (monto * 5) / 100
        
calcularPromedio = lambda lista: sum(lista) / len(lista) if lista else 0