# Your solution to Exercise 12

a = int(input(""))

b = a // 1000
c = (a // 100) % 10
d = (a // 10) % 10
e = a % 10

if b % 2 == 0:
    b = "*"
if c % 2 == 0:
    c = "*"
if d % 2 == 0:
    d = "*"
if e % 2 == 0:
    e = "*"
print(f'{b}{c}{d}{e}')
