# factorial n! = n * (n-1) * (n-2)*....

# find 20! = ?

# initial var
n = 20
f = 1

# loop process
while n != 0:
    f = f*n
    n = n-1

print('Factorial 20 =', f)
# 2432902008176640000
