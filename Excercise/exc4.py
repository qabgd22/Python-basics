PI = 3.14
r = eval(input('Unesite poluprečnik kruga: '))
if r>0:
    print('Obim kruga je: ', r*2*PI)
    print('Površina kruga je: ', r*r*PI)
else:
   print('Nedozvoljena vrednost za poluprečnik')

print()

i = 0
while i < 5:
   print(i)
   i = i + 1

# Output:
# 0
# 1
# 2
# 3
# 4

while 1:
    godine = eval(input('Godine: '))
    if godine > 100:
       print('prošao')
       continue
        
    if godine >0:
        break

print(godine)