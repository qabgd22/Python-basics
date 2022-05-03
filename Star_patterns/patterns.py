# Star pattern 5x10
# **********
# *        *
# *        *
# *        *
# **********

for i in range(5):
   if i >0 and i <=3:
       print('*',' '*6,'*')
   else:
       print('*'*10)


# Star pattern with right diagonal
# * * * * * 
# *     * *
# *   *   *
# * *     *
# * * * * *

n = int(input('Enter the dimension: '))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==(n-1) or j==(n-1) or j==(n-i-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Star pattern with left diagonal
# * * * * * 
# * *     *
# *   *   *
# *     * *
# * * * * *

n = int(input('Enter the dimension: '))
for i in range(n):
    for j in range(n):
        if  i==0 or j==0 or i==(n-1) or j==(n-1) or j==i:
            print("*", end = " ")
        else:
            print(" ", end=" ")
    print()

# Star pattern with two diagonals
# * * * * * 
# * *   * *
# *   *   *
# * *   * *
# * * * * *

n = int(input('Enter the dimension: '))
for i in range(n):
    for j in range(n):
        if  i==0 or j==0 or i==(n-1) or j==(n-1) or j==i or j==(n-i-1):
            print("*", end = " ")
        else:
            print(" ", end=" ")
    print()

# Triangle pattern
# *
# **
# ***
# ****
# *****

for i in range(5):
    print('*'*(i+1))
print()

# Triangle pattern
# *****
# ****
# ***
# **
# * 

for i in range(6,1,-1):
    print('*'*(i-1))
