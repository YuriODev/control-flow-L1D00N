# Your solution to Exercise 8

a = int(input(""))
b = int(input(""))

if (a // 100) == b or ((a // 10 ) % 10) == b or (a % 10):
    print("True")
else:
    print("False")
