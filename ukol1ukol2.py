jmeno = input("Zadejte sve jmeno: ")
vek = input("Zadejte svuj vek: ")
print(f"Ahoj, jmenuji se {jmeno} a je mi {vek} let.")


cislo1 = float(input("Zadejte prvni desetinne cislo: "))
cislo2 = float(input("Zadejte druhe desetinne cislo: "))
soucet = cislo1+cislo2
rozdil = cislo1-cislo2
soucin = cislo1*cislo2
if cislo2 !=0:
    podil = cislo1/cislo2
else:
    podil = None

print(f"Soucet: {soucet: .2f}")
print(f":Rozdil: {rozdil: .2f}")
print(f":Soucin: {soucin: .2f}")
if podil is not None:
    print(f"Podil: {podil: .2f}")
else:
    print("Podil nelze vypocitat (deleni nulou).")
