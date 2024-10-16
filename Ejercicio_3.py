'''Una oficina de atención al cliente tiene una cola de personas esperando para ser
atendidas. Implementa un programa que:
● Agregue clientes a la cola cuando lleguen.
● Atienda a los clientes en el orden en que llegaron.
● Permite consultar cuántos clientes quedan en la cola'''

cola_clientes = []

# Función que muestra el menú y gestiona las opciones del usuario
def menu():
    while True:
        # Imprime las opciones disponibles
        print('''
        1. Agregar cliente
        2. Atender cliente
        3. Consultar clientes en cola
        0. Salir
        ''')
        # Solicita una opción al usuario
        try:
            option = int(input('Ingrese una opción: '))
        except ValueError:
            print('Por favor, ingrese un número válido.')
            input('Presione Enter para continuar')
            continue

        # Procesa la opción seleccionada
        if option == 1:
            agregar_cliente()  # Opción para agregar un cliente
        elif option == 2:
            atender_cliente()  # Opción para atender al cliente
        elif option == 3:
            clientes_en_cola()  # Opción para consultar clientes en la cola
        elif option == 0:
            print('Saliendo del programa...')
            break  # Termina el programa
        else:
            print(f'Opción {option} incorrecta, intente nuevamente.')
            input('Presione Enter para continuar')  # Pausa antes de continuar

# Función para agregar un cliente a la cola
def agregar_cliente():
    nombre = input('Ingrese el nombre del cliente: ')  # Solicita el nombre del cliente
    cola_clientes.append(nombre)  # Agrega el nombre al final de la lista (cola)
    print(f'{nombre} ha sido agregado a la cola.')
    input('Presione Enter para continuar')  # Pausa antes de volver al menú

# Función para atender al siguiente cliente en la cola
def atender_cliente():
    if cola_clientes:  # Verifica si hay clientes en la cola
        cliente_atendido = cola_clientes.pop(0)  # Atiende (remueve) al primer cliente de la cola
        print(f'Cliente {cliente_atendido} ha sido atendido.')
    else:
        print('No hay clientes en la cola para atender.')
    input('Presione Enter para continuar')  # Pausa antes de volver al menú

# Función para consultar cuántos clientes quedan en la cola
def clientes_en_cola():
    print(f'Hay {len(cola_clientes)} cliente(s) en la cola.')  # Muestra el número de clientes en la cola
    input('Presione Enter para continuar')  # Pausa antes de volver al menú

# Ejecuta el menú principal
menu()
