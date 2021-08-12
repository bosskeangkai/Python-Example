# find the 20 numbers that we have to input from keyboard and find how many number that has more than 50 or less than 50

# input 20 values
n = 1
y = 0
z = 0

# condition
while n <= 5:
    num = int(input("Enter you value:"))

    if num > 50:
        y = y + 1
    else:
        z = z+1

    print("Number are ", num)

    n = n+1
print("The number more than 50 has {} numbers".format(y))
print("The number less than 50 has {} number".format(z))

# The number more than 50 has 2 numbers
# The number less than 50 has 3 number

# 3 option to insert value into string
# option1
# like a exam I did

# option 2
# print("The number less than 50 has {y} number")

# option 3 old school likes a C language %s %d
# stuff_in_string = "Shepherd %s is %d years old." % (shepherd, age)
