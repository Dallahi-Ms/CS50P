def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x, y = fraction.split('/')
    x = int(x)
    y = int(y)
    if x < 0 or y < 0:
        raise ValueError
    elif y == 0:
        raise ZeroDivisionError
    elif x > y:
        raise ValueError

    return round((x/y)*100)


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()
