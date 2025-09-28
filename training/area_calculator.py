import math

while(True):
    print("Alege forma geometrica: ")
    print("1. Dreptunghi")
    print("2. Patrat")
    print("3. Triunghi")
    print("4. Cerc")
    print("5. Iesire")
    forma = input()
    if forma.lower() == "dreptunghi" or forma.lower() == "1":
        print("Introduceti lungimea: ")
        lungime = int(input())
        print("Introduceti latimea: ")
        latime = int(input())
        print("aria dreptunghiului este: ", lungime*latime)
    elif forma.lower() == "patrat" or forma.lower() == "2":
        print("Introduceti lungimea laturii: ")
        lungime = int(input())
        print(" aria patratului este: ", lungime**2)
    elif forma.lower() == "triunghi" or forma.lower() == "3":
        print("Introduceti lungimea bazei: ")
        lungime = int(input())
        print("Introduceti inaltimea: ")
        inaltime = int(input())
        print(" aria triunghiului este: ", lungime*inaltime/2)
    elif forma.lower() == "cerc" or forma.lower() == "4":
        print("Introduceti lungimea razei: ")
        lungime = int(input())
        print(" aria cercului este: ", math.pi*lungime**2)
    elif forma.lower() == "iesire" or forma.lower() == "5":
        break
    else:
        print("Forma geometrica invalida")
        break
