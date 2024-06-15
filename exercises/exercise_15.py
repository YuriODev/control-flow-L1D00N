# Your solution to Exercise 15

a = int(input(""))
b = int(input(""))
c = int(input(""))
if c % 4 == 0 and c % 100 != 0 or c % 400 == 0:
    if a == 28 and b == 2:
        a += 1
    else:
        if b == 1 or b == 3 or b == 5 or b == 7 or b == 8 or b == 10 or b == 12:
            if a == 31:
                a = 1
                b += 1
            else:
                a += 1
        elif b == 2:
            if a == 28:
                a = 1
                b += 1
            else:
                a += 1
        else:
            if a == 30:
                a = 1
                b += 1
            else: 
                a += 1
else:
    if b == 1 or b == 3 or b == 5 or b == 7 or b == 8 or b == 10 or b == 12:
        if a == 31:
            a = 1
            b += 1
        else:
            a += 1
    elif b == 2:
        if a == 28:
            a = 1
            b += 1
        else:
            a += 1
    else:
        if a == 30:
            a = 1
            b += 1
        else: 
            a += 1
if b == 13:
    b = 1
print(f"{a:02d}.{b:02d}.{c:04d}")
