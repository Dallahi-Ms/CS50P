expression = input("Expression: ").split()
x = (float(expression[0]))
y = (float(expression[2]))
z = expression[1]

if z == '+':
    print(f"{(x + y):.1f}")
elif z == '-':
    print(f"{(x - y):.1f}")
elif z == '/':
    print(f"{(x / y):.1f}")
elif z == '*':
    print(f"{(x * y):.1f}")
else:
    print("Invalid operator")
