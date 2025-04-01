obleceni = ["kalhoty", "tricka", "saty", "sukne", "ponozky", "cepice"]
def obleceni_lenght():
    return len(obleceni)

print(obleceni_lenght())
for item in obleceni:
    print(item)

new_item = input("Enter a new element")
obleceni.append(new_item)
print(obleceni)

obleceni.remove("tricka")
print(obleceni)

obleceni.sort()
print(obleceni)

obleceni.reverse()
print(obleceni)

