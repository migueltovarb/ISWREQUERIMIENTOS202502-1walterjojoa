import csv
import os

ARCHIVO = "contactos.csv"

def cargar():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, 'r', encoding='utf-8') as f:
            return list(csv.DictReader(f))
    return []

def guardar(contactos):
    with open(ARCHIVO, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["nombre", "telefono", "correo", "cargo"])
        writer.writeheader()
        writer.writerows(contactos)

def registrar(contactos):
    print("\n=== REGISTRAR CONTACTO ===")
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    correo = input("Correo: ").strip()
    cargo = input("Cargo: ").strip()
    
    if not all([nombre, telefono, correo, cargo]):
        print(" Todos los campos son obligatorios")
        return
    
    if '@' not in correo:
        print(" Correo inválido")
        return
    
    if any(c['correo'].lower() == correo.lower() for c in contactos):
        print(" El correo ya existe")
        return
    
    contactos.append({"nombre": nombre, "telefono": telefono, "correo": correo, "cargo": cargo})
    guardar(contactos)
    print("Contacto registrado")

def buscar(contactos):
    print("\n=== BUSCAR CONTACTO ===")
    termino = input("Nombre o correo: ").strip().lower()
    
    resultados = [c for c in contactos if termino in c['nombre'].lower() or termino in c['correo'].lower()]
    
    if not resultados:
        print(" No se encontraron contactos")
        return
    
    print(f"\n{'Nombre':<20} {'Teléfono':<15} {'Correo':<30} {'Cargo':<20}")
    print("-" * 85)
    for c in resultados:
        print(f"{c['nombre']:<20} {c['telefono']:<15} {c['correo']:<30} {c['cargo']:<20}")

def listar(contactos):
    print("\n=== LISTA DE CONTACTOS ===")
    
    if not contactos:
        print("ℹ  No hay contactos")
        return
    
    print(f"\n{'Nombre':<20} {'Teléfono':<15} {'Correo':<30} {'Cargo':<20}")
    print("-" * 85)
    for c in contactos:
        print(f"{c['nombre']:<20} {c['telefono']:<15} {c['correo']:<30} {c['cargo']:<20}")

def eliminar(contactos):
    print("\n=== ELIMINAR CONTACTO ===")
    correo = input("Correo del contacto: ").strip().lower()
    
    for i, c in enumerate(contactos):
        if c['correo'].lower() == correo:
            contactos.pop(i)
            guardar(contactos)
            print(" Contacto eliminado")
            return
    
    print(" Contacto no encontrado")

def main():
    contactos = cargar()
    
    while True:
        print("\n" + "="*50)
        print("  SISTEMA DE CONTACTOS - ConnectMe")
        print("="*50)
        print("1. Registrar contacto")
        print("2. Buscar contacto")
        print("3. Listar contactos")
        print("4. Eliminar contacto")
        print("5. Salir")
        
        opcion = input("\nOpción: ").strip()
        
        if opcion == '1':
            registrar(contactos)
        elif opcion == '2':
            buscar(contactos)
        elif opcion == '3':
            listar(contactos)
        elif opcion == '4':
            eliminar(contactos)
        elif opcion == '5':
            print("\n¡Hasta pronto!")
            break
        else:
            print(" Opción inválida")

if _name_ == "_main_":
    main(dsefdf)