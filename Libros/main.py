#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

from Pila import *

class Libro:

    def __init__(self,nombre,genero,autor):
        self.nombre=nombre
        self.genero=genero
        self.autor=autor

pila = Pila()

pila.apilar(Libro("El Cartero de los Sueños","cuentos infantiles","Laura Gallego"))
pila.apilar(Libro("Un fantasma en apuros","cuentos infantiles","Laura Gallego"))
pila.apilar(Libro("Max ya no hace re¡r","cuentos infantiles","Laura Gallego"))
pila.apilar(Libro("Donde est  Alba?","cuentos infantiles","Laura Gallego"))
pila.apilar(Libro("Alba tiene una amiga muy especial","cuentos infantiles","Laura Gallego"))
pila.apilar(Libro("Por una rosa","relatos","Laura Gallego"))
pila.apilar(Libro("Mañana todavia. ","relatos","Laura Gallego"))
pila.apilar(Libro("El viaje del polizón","relatos","Laura Gallego"))
pila.apilar(Libro("Relatos insólitos","relatos","Laura Gallego"))
pila.apilar(Libro("Relatos de hoy II","relatos","Laura Gallego"))
pila.apilar(Libro("Atlántico. 30 historias de los dos mundos","relatos","Laura Gallego"))
pila.apilar(Libro("Historias para girar","relatos","Laura Gallego"))
pila.apilar(Libro("Topito Terremoto","cuentos ilustrados","Anna Llenas"))
pila.apilar(Libro("El Monstruo de Colores","cuentos ilustrados","Anna Llenas"))
pila.apilar(Libro("El buit","cuentos ilustrados","Anna Llenas"))
pila.apilar(Libro("Diario de las emociones","cuentos ilustrados","Anna Llenas"))
pila.apilar(Libro("Te quiero (casi siempre)","cuentos ilustrados","Anna Llenas"))
pila.apilar(Libro("Si yo fuera un gato","cuentos ilustrados","Paloma Sánchez"))
pila.apilar(Libro("Mis opuestos","cuentos ilustrados","Olga Cuellar"))
pila.apilar(Libro("Mi Mascota","cuentos","Yolanda Reyes"))
pila.apilar(Libro("Tumaco","cuentos","Oscar Pantoja"))
pila.apilar(Libro("Cuando el mundo era as¡","cuentos","Triunfo Arciniegas"))
pila.apilar(Libro("Mi primer libro de poes¡a colombiana","cuentos","Beatriz Helena Robledo"))

print("\n")
print("El tamaño de la pila es: ", pila.tamano())
print("\n")
print("----------------------------------")

while pila.es_vacia() == False:
    Libro = pila.desapilar()
    print("Apilamos libro")
    print("----------------------------------")
    print(Libro.nombre)
    print(Libro.genero)
    print(Libro.autor)
    print("El tamaño de la pila es: ", pila.tamano())
    print("\n")
    print("----------------------------------")

print("La pila esta vacia:", pila.es_vacia())

