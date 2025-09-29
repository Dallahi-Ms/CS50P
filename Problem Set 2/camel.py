text = input("camelCase: ")
snake_case = ''
for letter in text:
    if letter.isupper():
        snake_case += '_'

    snake_case += letter.lower()

print(f"snake_case: {snake_case}")
