string = '''P
weewwe
eweweew'''
print(string)

c = input('Unesite reč: ').lower()
if c == c[::-1]:
    print('Jeste palindrom')
else:
    print('Nije palindrom')

string = 'Ovo je neki string.'

for i in range(len(string)):
   if i !=5:
       print(string[i], end =' ')

#Output:
#O v o   j   n e k i   s t r i n g .      
print()

print(string[7:11])
# neki
print(string[:5])
# Ovo j
print(string[5:])
# e neki string.
print(string[-3:])
# .ng
print(string[:])
#Ovo je neki string.
print(string[1:11:2])
#v enk
print(string[::-1])
#.gnirts iken ej ovO