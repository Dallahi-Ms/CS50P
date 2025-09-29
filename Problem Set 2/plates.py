def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def length(a):
    if 2 <= len(a) <= 6:
        return True
    else:
        return False
def starts(b):
    if b[0].isalpha() and b[1].isalpha():
        return True
    else:
        return False
def marks(c):
    if c.isalnum():
        return True
    else:
        return False
def numbs(d):
    numbers = []
    for letter in d:
        if letter.isdigit():
            numbers.append(letter)
    if numbers:
        if numbers[0] == '0':
            return False
    return True
def num_inmid(e):
    for i in range(len(e)):
        if e[i].isdigit():
            if e[i:].isdigit():
                return True
            else:
                return False
    return True

def is_valid(s):
    if length(s) == True and starts(s) == True and marks(s) == True and \
            numbs(s) == True and num_inmid(s) == True:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
