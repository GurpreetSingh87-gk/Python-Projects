# Calculator App:-

'''
def Add(n1, n2):
    return n1 + n2

def Subtract(n1, n2):
    return n1 - n2

def Multiply(n1, n2):
    return n1 * n2

def Divide(n1, n2):
    return n1 / n2


def main():
    print("\n===== Calculator App =====\n")

    while True:
        print("\n1. Addition.")
        print("2. Subtraction.")
        print("3. Multiplication.")
        print("4. Divison.")
        print("5. Exit Program.")

        choice = input("\nEnter Your Choice:")

        if choice == "5":
            print("\n--> Thank You for Using Calculator!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("\nInvalid Choice!!")
            continue
        
        n1 = float(input("\nEnter Value 1 : "))
        n2 = float(input("Enter Value 2 : "))
    
        if choice == "1":
            result = Add(n1, n2)
            print("\nResult:", result)

        elif choice == "2":
            result = Subtract(n1, n2)
            print("\nResult:", result)

        elif choice == "3":
            result = Multiply(n1, n2)
            print("\nResult:", result)

        elif choice == "4":
            result = Divide(n1, n2)
            print("\nResult:", result)
            
main()            
'''
    
