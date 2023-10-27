from math import sqrt


def elso():
    szamsor = 0
    while szamsor < 150:
        if szamsor % 2 == 0:
            print(szamsor, end=", ")
        szamsor += 1
    print(150, end="")


def masodik():
    osztharom = 0
    sorszam = 1

    while sorszam <= 10:
        szam = int(input("Kérem adja meg a(z) " + str(sorszam) + ". számot: "))
        if szam % 3 == 0:
            osztharom += 1
        sorszam += 1
    print("A bekért számok alapján " + str(osztharom) + " olyan szám található, amely 3-mal osztható.")


def harmadik():
    szam = int(input("Kérem adjon meg egy számot, ami 10-zel osztható: "))
    while not (szam % 10 == 0):
        szam = int(input("Kérem adjon meg egy számot, ami 10-zel osztható: "))


def negyedik():
    szam = int(input("Kérem adjon meg egy olyan számot, ami kétjegyű és páros: "))
    while not ((((szam >= 10) and (szam <= 99)) or ((szam >= -99) and (szam <= -10))) and (szam % 2 == 0)):
        szam = int(input("Kérem adjon meg egy olyan számot, ami kétjegyű és páros: "))


def otodik():
    szam = int(input("Kérem adjon meg egy olyan számot, ami pozitív páratlan szám: "))
    while not ((szam > 0) and (szam % 2 == 1)):
        szam = int(input("Kérem adjon meg egy olyan számot, ami pozitív páratlan szám: "))


def hatodik():
    szam = int(input("Kérem adjon meg egy olyan számot, ami 3-al osztható vagy négyzetszám: "))
    while not ((szam % 3 == 0) or (sqrt(szam).is_integer())):
        szam = int(input("Kérem adjon meg egy olyan számot, ami 3-al osztható vagy négyzetszám: "))


def hetedik():
    a = float(input("Kérem adjon meg egy valós számot: "))
    b = float(input("Kérem adjon meg egy másik valós számot: "))
    c = float(input("Kérem adjon meg egy harmadik valós számot: "))
    if (a < b + c) and (b < a + c) and (c < a + b):
        print("A háromszög szerkeszthető.")
    else:
        print("A háromszög nem szerkeszthető.")


def nyolcadik():
    szoveg = input("Kérem adjon meg egy szöveget, ami legalább 3 karakteres: ")
    while not (len(szoveg) >= 3):
        szoveg = input("Kérem adjon meg egy szöveget, ami legalább 3 karakteres: ")
    print(str.upper(szoveg))


def kilencedik():
    szoveg = input("Kérem adjon meg egy szöveget, ami csupa kis betűs legalább 4 karakteres: ")
    while not (len(szoveg) >= 4 and szoveg.islower()):
        szoveg = input("Kérem adjon meg egy szöveget, ami csupa kis betűs legalább 4 karakteres: ")


def tiz():
    sorszam = 1
    osszeg = 0
    szamker = 0

    szam = int(input("Kérem adja meg a(z) " + str(sorszam) + ". egész számot: "))

    while not (szam == 0):
        while not (szam > 0):
            szam = int(input("Kérem adja meg a(z) " + str(sorszam) + ". egész számot: "))
        sorszam += 1
        szamker += 1
        szam = int(input("Kérem adja meg a(z) " + str(sorszam) + ". egész számot: "))
        osszeg += szam
    atlag = osszeg / szamker
    print(str(osszeg) + " / " + str(szamker) + " = " + str(round(atlag, 2)))