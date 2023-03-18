from random import randint

for i in range(5):
    try:
        broj1 = randint(1,10)
        broj2 = randint(1,10)
        print(broj1, '*', broj2, '=', end=' ')
        rez = eval(input())

        if rez == (broj1 * broj2):
            print('Tačno')
        else:
            print('Netačno! Tačan odgovor je:', broj1 * broj2)

    except SyntaxError:
        print('SyntaxError - Nije unet broj')
    except NameError:
        print('NameError - Unet tekst') 
print()

# Fibonacci
Fpr=0
Fsl=1

n = eval(input('Unesi broj članova niza: '))
        
for i in range(n):
    print(Fpr, end = ' ')
    f = Fpr + Fsl
    Fpr = Fsl
    Fsl = f
