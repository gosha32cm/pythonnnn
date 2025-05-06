# Popis programu
# Program počítá zvířata v zoo
# V zoo jsou tři druhy zvířat tygři, lvy a opice
# Program umožní uživateli provádět tři akce - přidat zvíře, odebrat zvíře a vypsat všechna zvířata
# Po jedné této akci se program automaticky zeptá jestli chce uživatel pokračovat


# Úkol
# Odkomentujte funkce
# Dopište funkce tak, aby fungoval celý program
# funkce pridej - má vstupní parametry zvire a počet - připočte k dané skupině tolik zvířat, kolik zadá uživatel(pocet)
# (pokud uživatel zadá neplatné zvíře vypíše se mu: "Neco si zadal špatně")
# funkce odeber - má vstupní parametry zvire a počet - odečte od dané skupiny tolik zvířat, kolik zadá uživatel(pocet)
# (pokud zadá neplatné zvíře, nebo bude chtít odbrat více zvířat než je aktuálně v zoo vypíše se mu: "Neco si zadal špatně")
# funkce vypis - vypíše všechna zvířata, která jsou aktuálně v zoo


# Tuto část dopiš

#def pridej(zvire, pocet):
    
#def odeber(zvire, pocet):
    
#def vypis():
    




# Tuto část nepřepisovat

# Počty zvířat v zoo
tygri = 0
lvy = 0
opice = 0

# informace pro cyklus zda se má opakovat či ne
opakovat = "ano"


while(opakovat=="ano"):

    # výpis akcí co lze provádět 
    print("Vyberte jednu z akcí(pište pouze číslo): ")
    print("1. přidat zvíře")
    print("2. odebrat zvíře")
    print("3. vypsat seznam zvířat")

    #načtení akce od uživatele
    cislo = int(input())
    
    if cislo==1:
        zvire = input("Zadejte zvířata která chcete přidat(tygri,lvy,opice)")
        pocet = int(input("Zadejte počet těchto zvířat"))
        pridej(zvire,pocet)
    elif cislo==2:
        zvire = input("Zadejte zvířata která chcete přidat(tygri,lvy,opice)")
        pocet = int(input("Zadejte počet těchto zvířat"))
        odeber(zvire,pocet)
    elif cislo==3:
        vypis()
    opakovat = input("Chcete opakovat program?(ano/ne)")
    
    
    
    
    
    def vytvor_utulek():
    return {}
def pridej_zvire(utulek, jmeno, druh, vek):
    utulek[jmeno] = {"druh": druh, "vek": vek}
def vypis_zvirata(utulek):
    for jmeno, info in utulek.items():
        druh = info["druh"]
        vek = info["vek"]
        if vek == 1:
            let = "rok"
        elif 2 <= vek <= 4:
            let = "roky"
        else:
            let = "let"
        print(f"{jmeno} je {druh} a je mu/jí {vek} {let}.")
def vypis_podle_druhu(utulek, druh):
    for jmeno, info in utulek.items():
        if info["druh"].lower() == druh.lower():
            vek = info["vek"]
            if vek == 1:
                let = "rok"
            elif 2 <= vek <= 4:
                let = "roky"
            else:
                let = "let"
            print(f"{jmeno} je {druh} a je mu/jí {vek} {let}.")
utulek = vytvor_utulek()
pridej_zvire(utulek, "Míca", "kočka", 3)
pridej_zvire(utulek, "Baryk", "pes", 5)
pridej_zvire(utulek, "Luska", "kočka", 1)
pridej_zvire(utulek, "Alík", "pes", 2)
pridej_zvire(utulek, "Bobek", "králík", 4)
print("Všechna zvířata v útulku:")
vypis_zvirata(utulek)
print("\nJen kočky v útulku:")
vypis_podle_druhu(utulek, "kočka")
