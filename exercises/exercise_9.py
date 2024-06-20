# Your solution to Exercise 9

a = int(input(""))

b = ((a // 10) % 10)
c = ((a // 100) + (a % 10))

if c > b:
    print(">")
elif c == b:
    print("=")
elif c < b:
    print("<")
