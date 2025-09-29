import random

while True:
    level = int(input('Level: '))
    if level <= 0:
        continue
    break

random_number = random.randint(1, level)


while True:
    try:
        guess = int(input('Guess: '))

        if guess <= 0:
            continue

        if guess > random_number:
            print('Too large!')
        elif guess < random_number:
            print('Too small!')
        else:
            print("Just right!")
            break

    except ValueError:
        pass
