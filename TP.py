import random
import MODULOTP
 
def main():
    
    # Verificar el login antes de continuar
    print("¡Bienvenido al sistema de COCINA INTELIGENTE!")
    if not MODULOTP.login():
        return  # Finaliza el programa si el login falla
   
    nombre = input("Ingrese su nombre: ")
    bienvenida = "Hola "+nombre
    print(bienvenida)
    
   # Inicializar listas y matriz
    listaMozo1 = []
    listaMozo2 = []
    matrizDatos = [["MOZO", "SECTOR", "MONTO"]]  # Encabezados de la matriz
 
    # Inicializar contadores y listas de reseñas
    clientesMozo1 = 0
    clientesMozo2 = 0
    reseñasMozo1 = []
    reseñasMozo2 = []
    
    # SE ELIGE EL SECTOR ENTRE 1 Y 2, Y TIRA UN NÚMERO AL AZAR ENTRE LOS DOS MOZOS
    sector = MODULOTP.obtenerSector()
    while sector != -1:
        sectorNombre = "Adentro" if sector == 1 else "Afuera"
        print(f"El sector elegido es {sectorNombre}")
        mozo = MODULOTP.asignarMozo()
        monto = random.randint(10000, 99999)
        print(f"El monto a pagar es de: ${monto}")
        comision = MODULOTP.calcularComision(monto)
        print(f"La comisión del mozo {mozo} es de ${comision}")
        
        # Almacenar la comisión y contar clientes
        if mozo == 1:
            listaMozo1.append(comision)
            clientesMozo1 += 1
        else:
            listaMozo2.append(comision)
            clientesMozo2 += 1
            
        # Agregar datos a la matriz
        matrizDatos.append([mozo, sectorNombre, monto])
 
        # Obtenemos reseña del cliente
        reseñaFinal = MODULOTP.reseñaCliente()
        if mozo == 1:
            reseñasMozo1.append(reseñaFinal)
        else:
            reseñasMozo2.append(reseñaFinal)
        # Pedir el sector nuevamente para continuar o terminar
        sector = MODULOTP.obtenerSector()
    
    print("CARGA FINALIZADA:")

    # Mostrar la matriz de datos iniciales
    MODULOTP.imprimirMatriz(matrizDatos)
    print()
    
    # Crear matriz de resultados finales con mozos, cantidad de clientes, y promedio de reseñas
    promedioReseñaMozo1 = MODULOTP.calcularPromedio(reseñasMozo1)
    promedioReseñaMozo2 = MODULOTP.calcularPromedio(reseñasMozo2)
   
    matrizResultados = [
        ["MOZO", "CANT. CLIENTES", "PROM. RESEÑAS"],
        [1, clientesMozo1, promedioReseñaMozo1],
        [2, clientesMozo2, promedioReseñaMozo2]
    ]
 
    # Mostrar la matriz de resultados finales
    MODULOTP.imprimirMatriz(matrizResultados)
    
    # Formatear y mostrar las comisiones alineadas por mozo
    print()
    print("LISTAS CON LAS COMISIONES DE LOS MOZOS")
    print("Mozo 1                  Mozo 2")
    maxLen = max(len(listaMozo1), len(listaMozo2))
    for i in range(maxLen):
        comision1 = f"{listaMozo1[i]}" if i < len(listaMozo1) else ""
        comision2 = f"{listaMozo2[i]}" if i < len(listaMozo2) else ""
        print(f"{comision1:<20}  {comision2:<20}")
        
if __name__ == "__main__":
    main()