def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def Modulus(x, y):
    return x & y
    
def Exponentiation(x, y):
    return x ** y
    
def Floor Division(x, y):
    return x // y

if __name__ == "__main__":
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Floor Division")
    
    choice = input("What Operatoin you gonna choose: ")

    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", Modulus(num1, num2))
        elif choice == '6':
            print("Result:", Exponentiation(num1, num2))
        else:
            print("Result:", Floor Division(num1, num2))
        
    else:
        print("Invalid choice")
