import time
import os
from tqdm import tqdm

def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
       os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
       os.system ("cls")

borrarPantalla()

print("")
print("------------------------------Calculadora PBAU------------------------------")
print("")
print("Hola :D, aquesta calculadora calcularà la teva nota de la PBAU")
print("")
print("--------------------------------Instruccions--------------------------------")
print("")
print("Hauràs d'introduir les notes que has obtingut a batxiller i a la PBAU")
print("Si no has cursat algun examen hauràs de posar de nota 0")
print("IMPORTANT tingues en compte no posar ningun caracter que no sigui un nombre")
print("En aquest cas el prgrama fallara i s'haurà de reiniciar")
print("")
print("--------------------------------Instruccions--------------------------------")
print("")
print("Perfavor, premeu intro per continuar")
print("")
input("------------------------------Calculadora PBAU------------------------------")
borrarPantalla()

def CalculNota():
    Nota_Batx = float(input("--> Nota del batxillerat: "))

    Catalan = float(input("--> Nota català: "))
    Castellano = float(input("--> Nota castellà: "))
    Ingles = float(input("--> Nota anglès: "))
    Historia = float(input("--> nota Història d'Espanya: "))
    Mates = float(input("--> Nota matemàtiques: "))

    Especifica1 = float(input("--> Nota específica 1: "))
    Especifica2 = float(input("--> Nota específica 2: "))
    print("")
    inici = time.time()

    Nota_Batx_final = Nota_Batx * 0.6
    Fase_General = Catalan + Castellano + Ingles + Historia + Mates
    Media_Fase_General = Fase_General / 5
    Nota_Fase_General = Media_Fase_General * 0.4

    Especifica1_Final = Especifica1 * 0.2
    Especifica2_Final = Especifica2 * 0.2

    if Especifica1 < 5:
        Especifica1_Final = 0

    if Especifica2 < 5:
        Especifica2_Final = 0

    Nota_Final_Sele = Nota_Batx_final + Nota_Fase_General + Especifica1_Final + Especifica2_Final

    for i in tqdm(range(1000000)):
        ...
    
    print("")
    
    time.sleep(0)
    fin = time.time()   
    tiempo = fin - inici


    print("FELICITATS! Has obtingut un", format(Nota_Final_Sele, '.3f'))
    print("")
    print("CALCULAT SATISFACTORIAMENT", "(""temps total:", tiempo,"sec"")")

    def reinicio():
        reiniciar = input("Desitja reiniciar? [Y/n]: ")
        if reiniciar == "Y":
            borrarPantalla()
            CalculNota()
        elif reiniciar == "y":
            borrarPantalla()
            CalculNota()
        elif reiniciar == "n":
            print("")
            print("Moltes gràcies per utilitzar aquest programa!")
            print("© 2023-2023 Miquel Estruch. All rights reserved")
            exit()
        else:
            print("No t'he entès.")
            reinicio()
    reinicio()

CalculNota()