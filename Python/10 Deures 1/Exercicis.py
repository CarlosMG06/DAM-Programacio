#!/usr/bin/env python3
import os
import random

def clearScreen():
    if os.name == 'nt':  # Si estàs en Windows
        os.system('cls')
    else:  # Si estàs en Linux o macOS
        os.system('clear')
clearScreen()

# Fes un programa que permeti a l'usuari introduir números i operacions. 
# El programa suma aquests números i mostra la suma 
# acumulada després de cada entrada. Si l'usuari escriu "sortir", 
# el programa acaba i mostra la suma final.
def suma_infinit():
    sumaAcumulada = 0
    while True:
        entrada = input("Introdueix un número o 'sortir' per acabar: ")
        
        if entrada.lower() == "sortir": break
        
        #L'entrada és un float vàlid si només conté digits i com a molt un punt decimal
        floatValid = True
        nombreDePunts = 0
        for c in entrada:
            if not(c.isdigit() or c == "."): floatValid = False
            if c == ".": nombreDePunts += 1
            if nombreDePunts > 1: floatValid = False

        if floatValid:
            sumaAcumulada += float(entrada)
            print(f"Suma de tots els números fins ara: {sumaAcumulada}")
        else:
            print("Entrada invàlida. Introdueix un número, si us plau.")

    print(f"La suma final és: {sumaAcumulada}")

# Escull un número aleatori entre 1 i 25, després fes que el programa multipliqui 
# aquest número per 2 repetidament, mostrant el resultat a cada iteració. 
# El bucle acaba quan el resultat supera 100. 
# Finalment retorna el número d'iteracions que han fet falta.
def multiplica_fins_100():
    n = random.randint(1, 25)
    print(f"El número aleatori generat és: {n}")

    iteracions = 0
    while n <= 100:
        n *= 2
        iteracions += 1
        print(f"Iteració {iteracions} - Resultat: {n}")
    
    print(f"Han fet falta {iteracions} iteracions per superar 100.")

# Fes un programa que mostri el següent menú
# Menú:
# 1 Saludar
# 2 Presentar
# 3 Vacilar
# 0 Sortir
# L'usuari ha de poder escriure el número o la opció (ignorant les majúscules)
# La opció 1 escriu "Hola colega"
# La opció 2 escriu "Sóc un programa molón"
# La opció 3 escriu "Pfff" o "De què vas?" de manera aleatòria
# La opció 0 surt del programa
def gestionar_menu():
    while True:
        print("Menú:\n1. Saludar\n2. Presentar\n3. Vacilar\n0. Sortir")
        choice = input("Tria una opció: ").lower()
        if choice == "1" or choice == "saludar": print("Hola colega")
        elif choice == "2" or choice == "presentar": print("Sóc un programa molón")
        elif choice == "3" or choice == "vacilar":
            rand = random.randint(0,1)
            if rand == 0: print("Pfff")
            else: print("De què vas?")
        elif choice == "0" or choice == "sortir":
            print("Sortint del programa...")
            break
        else: print("Opció invàlida.")

# Fes un programa que a partir de dos numeros aleatoris 
# entre 1 i 5 els ordena de major a menor i escriu 
# (X guions pel primer número, separats d'un espai) 
# tantes vegades com el segon número
def guions_ordenats():
    n1 = random.randint(1, 5)
    n2 = random.randint(1, 5)    
    text = ""
    for x in range(max(n1,n2)): 
        for y in range(min(n1,n2)): text += "-"
        text += " "
    print(text)

# Fes un programa que esculli una operació a l'atzar 
# (suma, resta, multiplicació i divisió). 
# Esculli dos números entre 1 i 10 a l'atzar i aleshores 
# apliqui la operació sobre el primer número 
# les vegades indicades pel segon número.
# Si la operació és dividir i el divisor és 0, ha de dir:
# No es pot dividir per 0
def operacio_aleatoria():
    operacions = ["suma","resta","multiplicació","divisió"]
    operacio = operacions[random.randint(0,3)]
    
    n1 = random.randint(0, 10)
    n2 = random.randint(0, 10)
    print(f"Operació escollida: {operacio}\nNombre a l'atzar: {n1}\nQuantitat de vegades: {n2}")

    resultat = n1
    if operacio == "suma": 
        for vegada in range(n2): resultat += n1
    elif operacio == "resta": 
        for vegada in range(n2): resultat -= n1
    elif operacio == "multiplicació": 
        for vegada in range(n2): resultat *= n1
    elif operacio == "divisió": 
        if n1 == 0: 
            print("No es pot dividir per 0.")
            return
        else:
            for vegada in range(n2): resultat /= n1

    print(f"Resultat: {resultat}")
