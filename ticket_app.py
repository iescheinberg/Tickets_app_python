import random
# Lista de ticket creados
lista_tickets = []

# Generar tickets aleatorios
def generar_id():
    return random.randint(1000, 9999)


# Crear ticket
def crear_ticket():
    while True:
        ticket_id = generar_id()
        print("Ingrese los datos para generar un nuevo Ticket: ")
        usuario = input("Ingrese su nombre: ")
        sector = input("Ingrese su sector: ")
        asunto = input("Ingrese asunto: ")
        mensaje = input("Ingrese un mensaje: ")
    
        nuevo_ticket = {
            "id": ticket_id,
            "nombre_usuario": usuario,
            "sector": sector,
            "asunto": asunto,
            "mensaje": mensaje,
        }
    
        lista_tickets.append(nuevo_ticket)
        print("="*30)
        print(f"Ticket generado correctamente!")
        print("="*30)
        
        print(f"Id: {ticket_id}")
        print(f"Nombre: {usuario}")
        print(f"Sector: {sector}")
        print(f"Asunto: {asunto}")
        print(f"Mensaje: {mensaje}")
        print("Recuerde su numero de Ticket")

        contuar = input("Desea generar un nuevo Ticket? (s/n): ").strip().lower()
        if contuar != "s":
            break

# Leer Tickets
def leer_tickets(id):
    for ticket in lista_tickets:
        if ticket["id"] == id:
            print("Ticket:")
            print(f"Id: {ticket['id']}")
            print(f"Nombre: {ticket['nombre_usuario']}")
            print(f"Sector: {ticket['sector']}")
            print(f"Asunto: {ticket['asunto']}")
            print(f"Mensaje: {ticket['mensaje']}")
            print("="*30)
            break
        else:
            print("Ticket no encontrado.\n")
            


def menu_tickets():
    while True:
        print("Bienvenido al sistema de Tickets")
        print("1- Generar nuevo Ticket")
        print("2- Leer Ticket")
        print("3- Salir")
        respuesta = int(input("Seleccione una acción: "))
        if respuesta == 3:
            print("Usted a salido.")
            break
        elif respuesta == 1:
            crear_ticket()
        elif respuesta == 2:
            id_ticket = int(input("Ingrese el número de Ticket: "))
            leer_tickets(id_ticket)
        else:
            print("Opción no válida.")

menu_tickets()
