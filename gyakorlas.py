def elso():
    beert = 0
    osszeg = 0
    ervenyes = 0
    hiba = 0
    szazalek = 0
    atlag = 0
    serules = 0

    letszam = int(input("Kérem, adja meg a résztvevők létszámát: "))

    i = 1
    while i <= letszam:
        eredmeny = int(input(f"Kérem, adja meg a(z) {i}. résztvevő eredményét másodpercben: "))

    if eredmeny < 0:
        print("Hiba: Érvénytelen eredmény! Negatív számot adott meg.")
        hiba += 1
    elif eredmeny > 0:
        ervenyes += 1
        osszeg += eredmeny
        i += 1
    else:
        serules += 1

    beert = ervenyes

    if letszam > 0:
        szazalek = (ervenyes / letszam) * 100

    if ervenyes > 0:
        atlag = osszeg / ervenyes

        print(f"1. Hányan értek be a célba sérülés nélkül: {beert} versenyző")
    if letszam > 0:
        print(f"2. Hány százalékuk teljesítette az adott szintet: {szazalek:.2f}%")
    if ervenyes > 0:
         print(f"3. Az érvényesen beérkezett és nem sérült résztvevők átlagos eredménye: {atlag:.2f} másodperc")
    if hiba == 0:
        print("Nem volt érvénytelen eredmény.")
    else:
        print(f"{hiba} alkalommal adtak meg érvénytelen eredményt.")