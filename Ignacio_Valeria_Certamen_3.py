#Importar Modulos
import random
import csv

#Listar Pedidos
pedido = []

#Menu Inicio
print("Bienvenido a CleanWasser\n")
print("1. Registar Pedido")
print("2. Listar Pedido")
print("3. Imprimir Hoja de ruta")
print("4. Buscar un pedido por ID")
print("5. Salir del programa")
print()
int(input("Ingrese un número (1 a 5): "))

#Datos del cliente
nombre_cliente = input("\nIngrese su Nombre y Apellido: ")
dirección = input("Ingrese su Dirección: ")
sector = input("Ingrese su sector: ")
print()

#Menu Dispensadores
print("Tipos de dispensadores\n")
print("1. Dispensador 6L")
print("2. Dispensador 10L")
print("3. Dispensador 20L")
print()

#Dispensadores a comprar
disp_6lts = int(input("Ingrese la cantidad a comprar del dispensador de 6L: "))
disp_10lts = int(input("Ingrese la cantidad a comprar del dispensador de 10L: "))
disp_20lts = int(input("Ingrese la cantidad a comprar del dispensador de 20L: "))
print()

#Registrado
print("Pedido Registrado exitosamente....")

#Pedido
pedidos = {
    "ID", id,
    "nombre", nombre_cliente, 
    "dirección", dirección, 
    "comuna", sector,
    "disp6l", disp_6lts,
    "disp10l", disp_10lts,
    "disp20l", disp_20lts,
}

#ID Pedido
id_pedido = random.randint(1000, 9999)

#Listar Todos los Pedido
print(pedidos)