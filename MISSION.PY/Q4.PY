# שאלה 4 סעיף א 

def multiple(a, b):
    if a == 0 or b == 0:
        return True
    return a % b == 0 or b % a == 0

def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    if multiple(x, y):
        print("One number is a multiple of the other")
    else:
        print("No number is a multiple of the other")

if __name__ == "__main__":
    main()

# שאלה 4 סעיף ב 

def is_multiple(a, b):
    return a % b == 0 or b % a == 0

def main():
    while True:
        x = int(input("Enter first number (-1 to stop): "))
        if x == -1:
            break

        y = int(input("Enter second number (-1 to stop): "))
        if y == -1:
            break

        if is_multiple(x, y):
            print("One number is a multiple of the other")
        else:
            print("No number is a multiple of the other")

if __name__ == "__main__":
    main()


