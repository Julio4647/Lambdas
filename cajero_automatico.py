saldo = 1000
salir = False
while not salir:
    print(f''' 1. Consulta de Saldo
    2. Retiro
    3. Deposito
    4. Salir''')
    opcion = int(input('Selecciona la operacion a realizar: '))
    if opcion == 1:
        print(f'Tu saldo es: {saldo}')
    elif opcion == 2:
        a = int(input('Que cantidad decea retirar: '))
        saldo -= a
    elif opcion == 3:
        b = int(input('Que cantidad deceas depositar: '))
        saldo += b
    elif opcion == 4:
        print('Saliendo del sistema.  Hasta pronto .....')
        salir = True
    else:
        print('Opcion invalida, prueba otra opcion')