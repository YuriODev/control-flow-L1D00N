# Your solution to Exercise 3

a = int(input("What number is your bet? "))
b = a % 2
if a < 0 or a > 36:
    print("The bet will not play!")
elif a == 0:
    print("Green")
elif a > 0 and a < 11 or a > 18 and a < 29:
    if b == 0:
        print("Black")
    else:
        print("Red")
else:
    if b == 0:
        print("Red")
    else:
        print("Black")
