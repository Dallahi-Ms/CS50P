import validators

def main():
    Email = input("What's your email adress?\n").strip()
    if validators.email(Email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
