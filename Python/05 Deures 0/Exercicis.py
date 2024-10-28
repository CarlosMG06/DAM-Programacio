#!/usr/bin/env python3
import math

# Conversió de graus Celsius a Fahrenheit
# Fórmula: Fahrenheit = (Celsius * 9/5) + 32
def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

# Conversió de graus Fahrenheit a Celsius
# Fórmula: Celsius = (Fahrenheit - 32) * 5/9
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Calcula l'Índex de Massa Corporal (IMC)
# Fórmula: IMC = pes / (altura ** 2)
def calcular_imc(pes, altura):
    return pes / altura ** 2

# Calcula la hipotenusa d'un triangle rectangle
# Utilitza el teorema de Pitàgores: hipotenusa = sqrt(catet1^2 + catet2^2)
def calcular_hipotenusa(catet1, catet2):
    return (catet1 ** 2 + catet2 ** 2) ** 0.5

# Comprova si un nombre és parell
# Per fer-ho, fem nombre % 2 i retornem si el resultat és 0
def es_parell(nombre):
    return nombre % 2 == 0

# Calcula l'àrea d'un cercle donat el radi
# Fórmula: Àrea = π * radi^2
def area_cercle(radi):
    return math.pi * radi**2

# Converteix minuts a hores i minuts
# Divideix minuts entre 60 per obtenir les hores i els minuts restants
def minuts_a_hores_minuts(minuts):
    hores = minuts // 60
    minutsRestants = minuts % 60
    return hores, minutsRestants

# Calcula el perímetre i l'àrea d'un rectangle
# Perímetre = 2 * (llargada + amplada)
# Àrea = llargada * amplada
def perimetre_i_area_rectangle(llargada, amplada):
    perimetre = 2 * (llargada + amplada)
    area = llargada * amplada
    return perimetre, area

# Calcula el preu final després d'un descompte percentual
# Preu final = preu inicial - (preu inicial * descompte_percent / 100)
def preu_final(preu_inicial, descompte_percent):
    return preu_inicial * (1 - descompte_percent / 100)

# Calcula l'interès simple
# Fórmula: Interès = capital * (taxa / 100) * temps
def interes_simple(capital, taxa, temps):
    return capital * (taxa / 100) * temps

# Converteix velocitat de km/h a m/s
# Fórmula: m/s = km/h * 1000 / 3600
def kmh_a_ms(velocitat_kmh):
    return velocitat_kmh * 1000 / 3600

# Exercici 1
# Fes un programa amb una variable que tingui el següent text: "La programació és com l'art de resoldre problemes"
# Després manipula aquest text per aconseguir mostrar:
# * La llargada de la frase
# * La subcadena 'art' en majúscules
# * Les lletres inicials de cada paraula concatenades en una cadena
# * La frase completa en majúscules i després en minúscules
# * La frase invertida paraula per paraula
def exercici1():
    frase = "La programació és com l'art de resoldre problemes"

    print(f'La llargada de la frase "{frase}" és de {len(frase)}')

    print("Subcadena 'art' en majúscules:", frase[frase.find("art"):frase.find("art")+len("art")].upper())

    posEspai1 = frase.find(" ")
    posEspai2 = frase.find(" ", posEspai1+1)
    posEspai3 = frase.find(" ", posEspai2+1)
    posEspai4 = frase.find(" ", posEspai3+1)
    posEspai5 = frase.find(" ", posEspai4+1)
    posEspai6 = frase.find(" ", posEspai5+1)
    posEspai7 = frase.rfind(" ")
    inicials = (frase[0] + frase[posEspai1+1] + frase[posEspai2+1] + frase[posEspai3+1] +
                frase[posEspai4+1] + frase[posEspai5+1] + frase[posEspai6+1] + frase[posEspai7+1])
    print("Inicials de cada paraula:", inicials)

    print("Frase en majúscules:", frase.upper())
    print("Frase en minúscules:", frase.lower())

    fraseInvertida = (frase[posEspai7+1:len(frase)] + frase[posEspai6:posEspai7] +
				      frase[posEspai5:posEspai6] + frase[posEspai4:posEspai5] + 
                      frase[posEspai3:posEspai4] + frase[posEspai2:posEspai3] + 
                      frase[posEspai1:posEspai2+1] + frase[0:posEspai1])
    print("Frase invertida paraula per paraula:", fraseInvertida)

# Exercici 2
# Fes un programa amb una variable que tingui el següent text: "Python és un llenguatge de programació potent i versàtil"
# Després manipula aquest text per aconseguir mostrar:
# * La posició de la paraula 'programació' dins la frase
# * Les paraules 'Python' i 'potent' concatenades en una sola paraula sense espais
# * La subcadena que comprèn des de 'un' fins a 'potent'
# * La frase amb totes les vocals reemplaçades per '*'
# * La frase amb la primera lletra de cada paraula en majúscula

# Fes servir ''.join(['*' if c in vocals else c for c in frase]) per canviar les vocals per '*'
# per exemple:
# frase = "Hola què tal"
# vocals = 'aeiouàèéíòóúüAEIOUÀÈÉÍÒÓÚÜ'
# fraseSenseVocals = ''.join(['*' if c in vocals else c for c in frase])
# print(fraseSenseVocals)

def exercici2():
    frase = "Python és un llenguatge de programació potent i versàtil"

    print("Posició de la paraula 'programació' dins la frase:", frase.find("programació"))

    pythonPotent = frase[0:6] + frase[frase.find("potent"):frase.find("potent")+len("potent")]
    print("Concatenació de 'Python' i 'potent':", pythonPotent)

    subcadena = frase[frase.find("un"):frase.find("potent")+len("potent")]
    print("Subcadena de 'un' a 'potent':", subcadena)
    
    vocals = 'aeiouàèéíòóúüAEIOUÀÈÉÍÒÓÚÜ'
    fraseSenseVocals = ''.join(['*' if c in vocals else c for c in frase])
    print("Frase amb vocals reemplaçades per '*':", fraseSenseVocals)

    posEspai1 = frase.find(" ")
    posEspai2 = frase.find(" ", posEspai1+1)
    posEspai3 = frase.find(" ", posEspai2+1)
    posEspai4 = frase.find(" ", posEspai3+1)
    posEspai5 = frase.find(" ", posEspai4+1)
    posEspai6 = frase.find(" ", posEspai5+1)
    posEspai7 = frase.find(" ", posEspai6+1)
    posEspai8 = frase.rfind(" ")
    fraseCapitalitzada = (frase[0:posEspai1+1].capitalize() + frase[posEspai1+1:posEspai2+1].capitalize() + frase[posEspai2+1:posEspai3+1].capitalize() + 
                          frase[posEspai3+1:posEspai4+1].capitalize() + frase[posEspai4+1:posEspai5+1].capitalize() + frase[posEspai5+1:posEspai6+1].capitalize() +
                          frase[posEspai6+1:posEspai7+1].capitalize() + frase[posEspai7+1:posEspai8+1].capitalize() + frase[posEspai8+1:len(frase)].capitalize())
    print("Frase amb cada paraula capitalitzada:", fraseCapitalitzada) 

# Exercici 3
# Fes un programa amb una variable que tingui el següent text: "Aprendre a programar és com aprendre un nou idioma"
# Després manipula aquest text per aconseguir mostrar:
# * El nombre de vegades que apareix la paraula 'aprendre'
# * La frase amb la paraula 'idioma' reemplaçada per 'superpoder'
# * Les tres primeres paraules de la frase
# * La frase amb les paraules en ordre invers
# * La frase original però sense espais

def exercici3():
    frase = "Aprendre a programar és com aprendre un nou idioma"
    
    print("Nombre de vegades que apareix la paraula 'aprendre':", frase.lower().count('aprendre'))
    
    print("Frase amb la paraula 'idioma' reemplaçada per 'superpoder':", frase.replace('idioma', 'superpoder'))
    
    posEspai1 = frase.find(" ")
    posEspai2 = frase.find(" ", posEspai1+1)
    posEspai3 = frase.find(" ", posEspai2+1)
    print("Les tres primeres paraules:", frase[0:posEspai3])
    
    posEspai4 = frase.find(" ", posEspai3+1)
    posEspai5 = frase.find(" ", posEspai4+1)
    posEspai6 = frase.find(" ", posEspai5+1)
    posEspai7 = frase.find(" ", posEspai6+1)
    posEspai8 = frase.rfind(" ")
    fraseInversa = (frase[posEspai8+1:len(frase)] + frase[posEspai7:posEspai8+1] + frase[posEspai6+1:posEspai7+1] + 
                    frase[posEspai5+1:posEspai6+1] + frase[posEspai4+1:posEspai5+1] + frase[posEspai3+1:posEspai4+1] + 
                    frase[posEspai2+1:posEspai3+1] + frase[posEspai1+1:posEspai2+1] + frase[0:posEspai1])
    print("Frase amb paraules en ordre invers:", fraseInversa)

    print("Frase sense espais:", frase.replace(' ', ''))


# Exercici 4
# Fes un programa amb una variable que tingui el següent text: "El coneixement és poder"
# Després manipula aquest text per aconseguir mostrar:
# * La llargada de la frase
# * La paraula 'poder' en majúscules
# * La frase repetida tres vegades amb un espai entre elles
# * La frase amb les vocals eliminades
# * La posició de la primera 'e' i de la darrera 'e' en la frase

def exercici4():
    frase = "El coneixement és poder"
    
    print(f'La llargada de la frase "{frase}" és de {len(frase)}')
    
    print("Subcadena 'poder' en majúscules:", frase[frase.find("poder"):len(frase)].upper())
    
    print(f"Frase repetida tres vegades: {frase} {frase} {frase}")
    
    vocals = 'aeiouàèéíòóúüAEIOUÀÈÉÍÒÓÚÜ'
    fraseSenseVocals = ''.join(['' if c in vocals else c for c in frase])
    print("Frase amb vocals eliminades:", fraseSenseVocals)
    
    print("Posició de la primera 'e':", frase.find('e'))
    print("Posició de la darrera 'e':", frase.rfind('e'))

# Exercici 5
# Fes un programa amb una variable que tingui el següent text: "La pràctica fa el mestre"
# Després manipula aquest text per aconseguir mostrar:
# * La frase amb cada paraula separada per un guió '-'
# * La frase amb l'ordre de les lletres de cada paraula invertit
# * La subcadena des del tercer fins al desè caràcter
# * La frase amb totes les consonants en majúscules i les vocals en minúscules
# * El nombre total de lletres sense comptar els espais

def exercici5():
    frase = "La pràctica fa el mestre"
    
    print("Frase amb cada paraula separada per guions:", frase.replace(' ', '-'))
    
    posEspai1 = frase.find(" ")
    posEspai2 = frase.find(" ", posEspai1+1)
    posEspai3 = frase.find(" ", posEspai2+1)
    posEspai4 = frase.rfind(" ")
    fraseParaulesInvertides = (frase[0:posEspai1][::-1] + frase[posEspai1:posEspai2+1][::-1] + frase[posEspai2+1:posEspai3+1][::-1] + 
						       frase[posEspai3+1:posEspai4+1][::-1] + frase[posEspai4+1:len(frase)][::-1])
    print("Frase amb les lletres de cada paraula invertides:", fraseParaulesInvertides)

    print("Subcadena del tercer al desè caràcter:", frase[2:10])
    
    vocals = 'aeiouàèéíòóúüAEIOUÀÈÉÍÒÓÚÜ'
    fraseCMajusVMinus = ''.join([c.lower() if c in vocals else c.upper() for c in frase])
    print("Consonants en majúscules i vocals en minúscules:", fraseCMajusVMinus)
    
    totalLletres = len(frase.replace(' ', ''))
    print("Nombre total de lletres (sense espais):", totalLletres)

# Exercici 6
# Fes un programa amb una variable que tingui el següent text: "   En un lugar de la Mancha, de cuyo nombre no quiero acordarme   "
# Després manipula aquest text per aconseguir mostrar:
# * La frase original sense espais al principi ni al final
# * La frase amb un ample total de 80 caràcters, centrada, omplint amb '-'
# * La frase amb un ample total de 80 caràcters, alineada a l'esquerra, omplint amb '*'
# * La frase amb un ample total de 80 caràcters, alineada a la dreta, omplint amb '.'
# * La llargada de la frase original i de la frase després d'aplicar strip()

def exercici6():
    frase = "   En un lugar de la Mancha, de cuyo nombre no quiero acordarme   "
    
    fraseStrip = frase.strip()
    print("Frase sense espais al principi ni al final:", fraseStrip)

    print("Frase centrada amb un ample de 80:", fraseStrip.center(80, '-'))
    print("Frase alineada a l'esquerra amb un ample de 80:", fraseStrip.ljust(80, '*'))
    print("Frase alineada a la dreta amb un ample de 80:", fraseStrip.rjust(80, '.'))
    
    print("Llargada original:", len(frase))
    print("Llargada després de strip():", len(fraseStrip))

# Exercici 7
# Fes un programa amb una variable que tingui el següent text: "****Benvinguts al curs de Python****"
# Després manipula aquest text per aconseguir mostrar:
# * La frase original sense els asteriscs del principi i del final
# * La frase sense els asteriscs només del principi
# * La frase sense els asteriscs només del final
# * La frase amb un ample total de 50 caràcters, centrada
# * La frase amb un ample total de 50 caràcters, alineada a la dreta

def exercici7():
    frase = "****Benvinguts al curs de Python****"
    
    fraseSenseAsteriscs = frase.strip('*')
    print("Frase sense asteriscs al principi i al final:", fraseSenseAsteriscs)
    
    print("Frase sense asteriscs al principi:", frase.lstrip('*'))
    print("Frase sense asteriscs al final:", frase.rstrip('*'))
    
    print("Frase centrada amb un ample de 50:", fraseSenseAsteriscs.center(50))
    print("Frase alineada a la dreta amb un ample de 50:", fraseSenseAsteriscs.rjust(50))

# Exercici 8
# Fes un programa amb una variable que tingui el següent text: "    Python és genial    "
# Després manipula aquest text per aconseguir mostrar:
# * La frase original amb els espais del principi eliminats
# * La frase original amb els espais del final eliminats
# * La frase amb un ample total de 30 caràcters, alineada a l'esquerra, omplint amb '-'
# * La frase amb un ample total de 30 caràcters, alineada a la dreta, omplint amb '+'
# * La frase amb un ample total de 30 caràcters, centrada, omplint amb '*'

def exercici8():
    frase = "    Python és genial    "
    
    print("Frase sense els espais del principi:", frase.lstrip())
    print("Frase sense els espais del final:", frase.rstrip())
    
    print("Frase alineada a l'esquerra amb un ample de 30:", frase.strip().ljust(30, '-'))
    print("Frase alineada a la dreta amb ample 30:", frase.strip().rjust(30, '+'))
    print("Frase centrada amb ample 30:", frase.strip().center(30, '*'))

# Exercici 9
# Crea un programa que mostri un menú tipus:
# *********************************Menú Principal*********************************
#             1. Veure perfil                         4. Configuració             
#          2. Canviar contrasenya                         5. Ajuda                
#                3. Sortir                            6. Tancar sessió  
# Sense utilitzar bucles 'for' ni 'while', i fent servir les funcions ljust, center, rjust, etc.
# El programa ha de mostrar el menú amb dues columnes d'opcions una al costat de l'altra.

def exercici9():
    titol = "Menú Principal".center(80, '*')

    opcio1 = "1. Veure perfil".center(40)
    opcio2 = "2. Canviar contrasenya".center(40)
    opcio3 = "3. Sortir".center(40)
    opcio4 = "4. Configuració".center(40)
    opcio5 = "5. Ajuda".center(40)
    opcio6 = "6. Tancar sessió".center(40)

    print(titol)
    print(opcio1+opcio4)
    print(opcio2+opcio5)
    print(opcio3+opcio6)
