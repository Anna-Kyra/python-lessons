number1 = float(input("Enter first number: ")) # Met float erachter kan je het antwoord meteen naar een float veranderen
operator = input("Enter operator: ")
number2 = float(input("Enter second number: "))

if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "/":
    print(number1 / number2)
elif operator == "*":
    print(number1 * number2)
else:
    print("Invalid operator") # Basically de error