# Your solution to Exercise 17

a = int(input("please enter a 6 digit number"))

b = a % 10
c = (a // 10) % 10
d = (a // 100) % 10
e = (a // 1000) % 10
f = (a // 10000) % 10
g = a // 100000
if (b + c + d) == (e + f + g):
    print("Happy")
else:
    print("Ordinary")
