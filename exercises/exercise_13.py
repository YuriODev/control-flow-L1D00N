# Your solution to Exercise 13

a = int(input(""))

b = a // 1000
c = (a // 100) % 10
d = (a // 10) % 10
e = a % 10

if b == c or b == d or b == e or c == d or c == e or d == e:
    print("False")
else:
    print("True")
