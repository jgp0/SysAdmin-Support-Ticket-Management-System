import csv
import time

ruta_csv = 'data/tickets.csv'

# Función para crear un nuevo ticket
def crear_ticket(usuario, descripcion, urgencia):
    # Cargar los tickets existentes desde el archivo CSV
    tickets = cargar_tickets_csv()

    ticket_id = len(tickets) + 1
    estado = "Abierto"
    fecha_creacion = time.strftime("%Y-%m-%d %H:%M:%S")
    tickets[ticket_id] = {
        "Ticket ID": ticket_id,
        "Usuario": usuario,
        "Descripcion": descripcion,
        "Urgencia": urgencia,
        "Estado": estado,
        "Fecha de Creacion": fecha_creacion,
    }
    guardar_tickets_csv(tickets)
    return ticket_id

# Función para cambiar el estado de un ticket
def cambiar_estado(ticket_id, nuevo_estado):
    # Cargar los tickets existentes desde el archivo CSV
    tickets = cargar_tickets_csv()

    if ticket_id in tickets:
        tickets[ticket_id]["Estado"] = nuevo_estado
        guardar_tickets_csv(tickets)
        return True
    return False

# Función para listar todos los tickets
def listar_tickets():
    # Cargar los tickets existentes desde el archivo CSV
    return cargar_tickets_csv()

# Función para guardar los tickets en un archivo CSV
def guardar_tickets_csv(tickets):
    with open(ruta_csv, mode="w", newline="") as archivo_csv:
        campos = ["Ticket ID", "Usuario", "Descripcion", "Urgencia", "Estado", "Fecha de Creacion"]
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
        escritor_csv.writeheader()
        for ticket_info in tickets.values():
            escritor_csv.writerow(ticket_info)

# Función para cargar los tickets desde un archivo CSV
def cargar_tickets_csv():
    try:
        with open(ruta_csv, mode="r") as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            tickets = {}
            for fila in lector_csv:
                ticket_id = int(fila["Ticket ID"])
                fila["Ticket ID"] = ticket_id  # Convertir el campo a int
                tickets[ticket_id] = fila
            return tickets
    except FileNotFoundError:
        # El archivo CSV no existe todavía, retornamos un diccionario vacío
        return {}

# Ejemplo de uso
if __name__ == "__main__":
    while True:
        print("\nSistema de Gestión de Tickets de Soporte Técnico")
        print("1. Crear Ticket")
        print("2. Listar Tickets")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario = input("Nombre de Usuario: ")
            descripcion = input("Descripción del Problema: ")
            urgencia = input("Nivel de Urgencia (Alto/Medio/Bajo): ")
            ticket_id = crear_ticket(usuario, descripcion, urgencia)
            print(f"Ticket creado con ID {ticket_id}")

        elif opcion == "2":
            tickets = listar_tickets()
            for ticket_id, ticket_info in tickets.items():
                print("\nTicket ID:", ticket_info["Ticket ID"])
                print("Usuario:", ticket_info["Usuario"])
                print("Descripción:", ticket_info["Descripcion"])
                print("Urgencia:", ticket_info["Urgencia"])
                print("Estado:", ticket_info["Estado"])
                print("Fecha de Creación:", ticket_info["Fecha de Creacion"])

        elif opcion == "3":
            break