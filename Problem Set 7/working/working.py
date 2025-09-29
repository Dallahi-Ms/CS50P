# import re


# def main():
#     print(convert(input("Hours: ")))

# def convert(s):
#     pattern = r"^((?:0?[0-9])|(?:1[0-2])):?([0-5][0-9])? ((?:A|P)M) to ((?:0?[0-9])|(?:1[0-2])):?([0-5][0-9])? ((?:A|P)M)$"
#     match = re.search(pattern, s)
#     num1 = match.group(1)
#     nu1 = int(num1)
#     num2 = match.group(4)
#     nu2 = int(num2)
#     if match.group(3) == "AM" and nu1 == 12:
#         nu1 = 0
#     if match.group(6) == "AM" and nu2 == 12:
#         nu2 = 0
#     if match.group(3) == "PM":
#         nu1 += 12
#         if nu1 >= 24:
#             nu1 = 12
#     if match.group(6) == "PM":
#         nu2 += 12
#         if nu2 >= 24:
#             nu2 = 12
#     if match.group(2):
#         num3 = match.group(2)
#         nu3 = int(num3)
#     else:
#         nu3 = 0
#     if match.group(5):
#         num4 = match.group(5)
#         nu4 = int(num4)
#     else:
#         nu4 = 0

#     return f"{nu1:02}:{nu3:02} to {nu2:02}:{nu4:02}"

# if __name__ == "__main__":
#     main()


import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^((?:0?[0-9])|(?:1[0-2])):?([0-5][0-9])? ((?:A|P)M) to ((?:0?[0-9])|(?:1[0-2])):?([0-5][0-9])? ((?:A|P)M)$"
    if match := re.search(pattern, s):
        h1, f1, h2, f2 = match.group(1), match.group(3), match.group(4), match.group(6)
        if match.group(2):
            m1 = match.group(2)
        else:
            m1 = 0
        if match.group(5):
            m2 = match.group(5)
        else:
            m2 = 0
        h1, m1, h2, m2 = int(h1), int(m1), int(h2), int(m2)
        if f1 == "PM" and h1 != 12:
            h1 += 12
        if f2 == "PM" and h2 != 12:
            h2 += 12
        if f1 == "AM" and h1 == 12:
            h1 = 0
        if f2 == "AM" and h2 == 12:
            h2 = 0
        if not m1:
            m1 = 0
        if not m2:
            m2 = 0

        return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()




