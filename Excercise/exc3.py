# Output:
# Hello! 0
# Hello! 2
# Hello! 4
# Hello! 6
# Hello! 8
# Hello! 10

for i in range(0, 11, 2):
   print('Hello!', end=' ')
   print(i)
print()

# Output:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0

for i in range(10,-1,-1):
   print(i)
print()

# Output:
# ********************
# *                  *
# *                  *
# *                  *
# *                  *
# *                  *
# *                  *
# *                  *
# *                  *
# ********************

for i in range(10):
   if i == 0:
       print('*' * 20)
   elif i == 9:
       print('*' * 20)
   else:
       print('*', ' '*16, '*') 