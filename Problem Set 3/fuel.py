def fraction_maker():
    if x/y <= 0.01 :
        a = 'E'
    elif x/y >= 0.99:
        a = 'F'
    else:
        a = f'{(x/y)*100:.0f}%'
    print(a)

while True :
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)

        if (x < 0) or (y < 0):
            continue
        elif x is float or y is float or x/y > 1:
            continue

        fraction_maker()
        break

    except ZeroDivisionError:
        pass
    except ValueError:
        pass
