# Your solution to Exercise 7

n1 = float(input(""))
n2 = float(input(""))
a = input("")

if a == "+":
    print(n1 + n2)
elif a == "-":
    print(n1 - n2)
elif a == "/":
    if n2 == 0:
        print("Division by 0!")
    else:
        print(n1 / n2)
elif a == "*":
    print(n1 * n2)
elif a == "mod":
    print(n1 % n2)
elif a == "pow":
    print(n1 ** n2)
