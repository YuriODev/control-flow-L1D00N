# Your solution to Exercise 4

a = int(input("enter the level"))

if a > 12 or a < 1:
    print("level is absent")
elif a > 9:
    print("high level")
elif a > 6:
    print("sufficient level")
elif a > 3:
    print("average level")
else:
    print("initial level")
