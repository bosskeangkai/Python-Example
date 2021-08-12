# input number 3 digit 10 numbers and find sum and avg

# initial var
n = 1
sum = 0

# condition
while n <= 10:
    num = int(input("Enter your number:"))
    sum = sum + num
    print(num)

    n = n+1

avg = sum/2

print("Total sum =", sum)
print("The Average of number=", avg)


# Total sum = 55 The Average of number = 27.5
