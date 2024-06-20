# Your solution to Exercise 6

x1 = float(input(""))
y1 = float(input(""))
x2 = float(input(""))
y2 = float(input(""))

if x1 * y1 > x2 * y2:
    print("A is further from the origin.")
elif x1 * y1 == x2 * y2:
    print("A and B are at the same distance from the origin.")
else:
    print("B is further from the origin.")
