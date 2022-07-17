ime = input("Unesite svoje ime: ")
godine = eval(input("Koliko godina imate? "))

if ime != "":
    print("Dobro dosli ", ime)
else:
    print("Niste uneli ime!")

if godine <= 0:
    print("Uneli ste nedozvoljene vrednosti")
if godine >= 18:
    print("Punoletni ste!")
if godine < 18:
    print("Maloletni ste!")

racun = eval(input("Unesite iznos vaseg racuna: "))
baksis = eval(input("Unesite baksis u procentima: "))

if racun < 0:
    print("Uneli ste nedozvoljene vrednosti")
if baksis < 0:
    print("Uneli ste nedozvoljene vrednosti")

b = (racun * baksis) / 100

print("Vas racun iznosi ", racun)
print("Baksis iznosi ", b)
print("Vas ukupan racun iznosi ", racun + b)