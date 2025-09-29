import random

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        tries = 3
        while tries > 0:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer != x + y:
                    tries -= 1
                    print("EEE")
                else:
                    score += 1
                    break

            except ValueError:
                print("EEE")
                tries -= 1

            if tries == 0:
                print(f"{x} + {y} = {x + y}")


    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        a = random.randint(0, 9)
    elif level == 2:
        a = random.randint(10, 99)
    else:
        a = random.randint(100, 999)

    return a



if __name__ == "__main__":
    main()

