import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    j = r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])"
    pattern = rf"^{j}\.{j}\.{j}\.{j}$"
    if re.search(pattern, ip):
        return True
    else:
        return False


if __name__ == "__main__" :
    main()
