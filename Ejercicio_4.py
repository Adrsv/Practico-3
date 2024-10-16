'''En un cine, se dispone de 70 butacas distribuidas en 7 filas con 10 columnas cada una. El
objetivo es desarrollar un sistema de turnero que permita visualizar un mapa interactivo de
las butacas, mostrando cuáles están vacías y cuáles han sido reservadas .
Al momento de reservar un asiento , el sistema debe registrar el nombre y el teléfono del
cliente, y marcar el asiento como ocupado o reservado en el mapa. Además, se debe
proporcionar la funcionalidad de consultar la información del cliente que ha reservado un
lugar específico, permitiéndole ver sus datos de contacto '''

# Inicializa el cine con 7 filas y 10 columnas (70 butacas) vacías
butacas= [[{'estado': 'vacío', 'cliente': None} for _ in range(10)] for _ in range(7)]

# Función para mostrar el mapa de butacas
def mostrar_mapa():
    print("\nMapa de butacas (O = ocupado, V = vacío):")
    for i, fila in enumerate(butacas):
        fila_str= ''
        for butaca in fila:
            if butaca['estado'] == 'vacío':
                fila_str += 'V '  # V de vacío
            else:
                fila_str += 'O '  # O de ocupado
        print(f'Fila {i + 1}: {fila_str}')
    print()  # Espacio entre el mapa y el siguiente bloque de salida
    input('Presione Enter para continuar')

# Función para reservar una butaca
def reservar_butaca():
    try:
        fila = int(input('Ingrese el número de fila (1-7): ')) - 1
        columna = int(input('Ingrese el número de columna (1-10): ')) - 1

        if butacas[fila][columna]['estado'] == 'vacío':
            nombre= input('Ingrese el nombre del cliente: ')
            telefono= input('Ingrese el teléfono del cliente: ')
            butacas[fila][columna]= {'estado': 'reservado', 'cliente': {'nombre': nombre, 'telefono': telefono}}
            print(f'Butaca en Fila {fila+1}, Columna {columna+1} ha sido reservada para {nombre}.\n')
            input('Presione Enter para continuar')
        else:
            print('La butaca seleccionada ya está reservada.\n')
            input('Presione Enter para continuar')  
    except (IndexError, ValueError):
        print('Error: Fila o columna inválida. Intente de nuevo.\n')
        input('Presione Enter para continuar')
        
# Función para consultar información de una butaca
def consultar_butaca():
    try:
        fila= int(input('Ingrese el número de fila (1-7): ')) - 1
        columna= int(input('Ingrese el número de columna (1-10): ')) - 1

        butaca= butacas[fila][columna]
        if butaca['estado'] == 'reservado':
            cliente= butaca['cliente']
            print(f'La butaca en Fila {fila+1}, Columna {columna+1} está reservada por {cliente["nombre"]}.\nTeléfono: {cliente["telefono"]}\n')
            input('Presione Enter para continuar')
        else:
            print('La butaca seleccionada está vacía.\n')
            input('Presione Enter para continuar')
    except (IndexError, ValueError):
        print('Error: Fila o columna inválida. Intente de nuevo.\n')
        input('Presione Enter para continuar')

# Menú principal del sistema
def menu():
    while True:
        print('''
        1. Mostrar mapa de butacas
        2. Reservar una butaca
        3. Consultar información de una butaca
        0. Salir
        ''')
        try:
            opcion = int(input('Ingrese una opción: '))
            if opcion == 1:
                mostrar_mapa()
            elif opcion == 2:
                reservar_butaca()
            elif opcion == 3:
                consultar_butaca()
            elif opcion == 0:
                print('Saliendo del sistema...')
                break
            else:
                print('Opción inválida. Intente nuevamente.\n')
                input('Presione Enter para continuar')
        except ValueError:
            print('Error: Debe ingresar un número válido.\n')
            input('Presione Enter para continuar')

# Iniciar el programa
menu()
