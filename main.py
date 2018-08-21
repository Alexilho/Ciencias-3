#!/usr/bin/python
# -*- coding: utf-8 -*-

from cola import *

class Estudiante:

    def __init__(self,nombre,codigo,placa):
        self.nombre=nombre
        self.codigo=codigo
        self.placa=placa

colaa = Cola()

colaa.encolar(Estudiante("Cristian Alexander Bravo","20142020999","RZS133"))
colaa.encolar(Estudiante("Manuel Enrique Restrepo","20132020111","WIF125"))
colaa.encolar(Estudiante("Ricardo Alberto Rusinque","20102020444","XLR258"))
print("\n")
print("El tamaño de la cola es: ", colaa.tamano())
print("\n")
print("----------------------------------")
while colaa.es_vacia() == False:
    print("Atiende estudiante")
    print("----------------------------------")
    estudiante = colaa.desencolar()
    print(estudiante.nombre)
    print(estudiante.codigo)
    print(estudiante.placa)
    print("El tamaño de la cola es: ", colaa.tamano())
    print("\n")
    print("----------------------------------")

print("La pila esta vacia:", colaa.es_vacia())
