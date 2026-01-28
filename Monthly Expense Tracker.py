# Monthly Expense Tracker:-
# -----------------------

'''
import matplotlib.pyplot as plt

def get_expenses():
    expenses = {}

    print("Enter Your Monthly Expenses:\n")

    expenses["Food"] = float(input("Food: Rs."))
    expenses["Rent"] = float(input("Rent: Rs."))
    expenses["Transport"] = float(input("Transport: Rs."))
    expenses["Electricity"] = float(input("Electricity: Rs."))
    expenses["Internet"] = float(input("Internet: Rs."))
    expenses["Other"] = float(input("Others: Rs."))
    
    return expenses

def show_expenses(expenses):

    total = sum(expenses.values())
    print("----------------------------")
    print("\nTotal Expenses: Rs.", total)


def show_pie_chart(expenses):

    categories = list(expenses.keys())
    values = list(expenses.values())

    custom_colors=["lightblue", "red", "purple", "yellow", "orange", "green"]

    plt.figure()
    plt.pie(values, labels=categories, colors=custom_colors, autopct="%1.1f%%")
    plt.title("Monthly Expense Distribution")

    plt.show()

def show_bar_chart(expenses):

    categories = list(expenses.keys())
    values = list(expenses.values())

    plt.figure()
    plt.bar(categories, values, color=["lightblue", "red", "purple", "yellow", "orange", "green"])
    plt.xlabel("Category")
    plt.ylabel("Amount (Rs.)")

    plt.show()
    
def main():

    print("\n====== Monthly Expense Tracker ======\n")

    expenses = get_expenses()
    show_expenses(expenses)

    while True:
        print("\n==== Choose Options For Data Visualization ====\n")

        print("1. Show Pie Chart.")
        print("2. Show Bar Chart.")
        print("3. Exit.")

        choice = input("\nEnter Your Choice:")

        if choice == "1":
            show_pie_chart(expenses)

        elif choice == "2":
            show_bar_chart(expenses)

        elif choice == "3":
            print("\nThank You!")
            break
        
        else:
            print("Invalid Choice!")
        
main()    
'''
