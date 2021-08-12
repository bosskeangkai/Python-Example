# find the total sum 1+3+5+7+...+100

# initial var
n = 1
sum = 0

# process we see while is the loop that like a if-else statement , while is if true run if false stop
while n <= 100:
    sum = sum+n
    n = n+2

print("Total sum =", sum)
# Total sum = 2500
