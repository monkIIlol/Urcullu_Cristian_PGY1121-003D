from os import system
system('cls')

import csv
import random
from statistics import geometric_mean

a = 0
trabajadores = [["Juan Pérez"],["María García"],["Carlos López"],["Ana Martínez"],["Pedro Rodríguez"],["Laura Hernández"],["Miguel Sánchez"],["Isabel Gómez"],["Francisco Díaz"],["Elena Fernández"]]


def asignar_sueldos():
    global a

    for pos, i in enumerate(trabajadores):
        aleat = random.randint(300000,2500000)
        trabajadores[pos].append(aleat)

    print("\nSueldos asignados\n")

    a += 1

    return trabajadores

def clasificar_sueldos():

    menores_800000 = 0
    lista_menores_800000 = []

    entre_tal_y_tal = 0
    lista_entre = []

    superiores_2000000 = 0
    lista_superiores_2000000 = []

    Total_sueldos = 0

    #-----menores a 800.000-----------

    for trabajador in trabajadores:
        if trabajador[1] < 800000:
            menores_800000 += 1 
            lista_menores_800000.append(trabajador[0:2])
            Total_sueldos += trabajador[1]
    
    #print(lista_menores_800000)               #probar

    #-----entre 800.000 y 2.000.000----

    for trabajador in trabajadores:
        if trabajador[1] <= 2000000 and trabajador[1] >= 800000:
            entre_tal_y_tal += 1
            lista_entre.append(trabajador[0:2])
            Total_sueldos += trabajador[1]

    #print(lista_entre)                        #probar

    #---------Superiores a 2.000.000---

    for trabajador in trabajadores:
        if trabajador[1] > 2000000:
            superiores_2000000 += 1
            lista_superiores_2000000.append(trabajador[0:2])
            Total_sueldos += trabajador[1]

    #print(lista_superiores_2000000)          #probar

    #--------------mostrar lista---------------------

    print(f"""

Sueldos menores a $800.000 Total: {menores_800000}

Nombre empleado          Sueldo""")
    
    for trabajador in lista_menores_800000:
        print(f"""{trabajador[0]}          {trabajador[1]}""")
        
    print(f"""

Sueldos entre $800.000 y $2.000.000 Total: {entre_tal_y_tal}

Nombre empleado          Sueldo""")
    
    for trabajador in lista_entre:
        print(f"""{trabajador[0]}          {trabajador[1]}""")
    
    print(f"""

Sueldos superiores a $2.000.000 Total: {superiores_2000000}

Nombre empleado          Sueldo""")
    
    for trabajador in lista_superiores_2000000:
        print(f"""{trabajador[0]}          {trabajador[1]}""")

    print(f"\nTOTAL SUELDOS: {Total_sueldos}")

def ver_estadisticas():
    
    lista_sueldos = []

    for trabajador in trabajadores:
        lista_sueldos.append(trabajador[1])
    
    geo = geometric_mean(lista_sueldos)

    Sueldo_más_alto = 0

    for trabajador in trabajadores:
        if trabajador[1] > Sueldo_más_alto:
            Sueldo_más_alto = trabajador[1]

    #print(Sueldo_más_alto)

    Sueldo_más_bajo = 999999999999999

    for trabajador in trabajadores:
        if trabajador[1] < Sueldo_más_bajo:
            Sueldo_más_bajo = trabajador[1]

    #print(Sueldo_más_bajo)

    suma = 0

    for trabajador in trabajadores:
        suma += trabajador[1]

    prom = suma / 10

    #print(prom)

    print(f"""
Sueldo más alto: {Sueldo_más_alto}
Sueldo más bajo: {Sueldo_más_bajo}
Promedio de sueldos: {prom}
Media geométrica: {round(geo,2)}""")

def reporte_sueldos():

    lista = []

    print(f"""
Nombre empleado          Sueldo base          Descuento salud          Descuento AFP          Sueldo Líquido\n""")
    for trabajador in trabajadores:

        desc_salud = trabajador[1] * 0.07
        desc_afp = trabajador[1] * 0.12
        liq = trabajador[1] - (desc_afp + desc_salud)

        print(f"""{trabajador[0]}              {round(trabajador[1])}                  {round(desc_salud)}                {round(desc_afp)}                {round(liq)}""")

def salir():
    pass

while True:
    op = input("""
1. Asignar sueldos
2. Clasificar sueldos
3. Ver estadísticas
4. Reporte de sueldos
5. Salir del programa

: """)
    match op:
        
        case "1":
            asignar_sueldos()

        case "2":
            if a >= 1:
                clasificar_sueldos()
            else:
                print("No has asignado los sueldos...")

        case "3":
            if a >= 1:
                ver_estadisticas()
            else:
                print("No has asignado los sueldos...")

        case "4":
            if a >= 1:
                reporte_sueldos()
            else:
                print("No has asignado los sueldos...")

        case "5":
            salir()
            print("""
Finalizando programa...
Desarrollado por Cristian Urcullú
RUT 21.467.936-1""")
            break
