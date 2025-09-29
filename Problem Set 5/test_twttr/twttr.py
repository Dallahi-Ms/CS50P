def main():
    Input = input('Input: ')
    print(f"Ouput: {shorten(Input)}")


def shorten(word):
    vowels = 'aoeiu'
    Output = ''

    for letter in word:
        if letter.lower() not in vowels:
            Output += letter
    return Output


if __name__ == "__main__":
    main()
