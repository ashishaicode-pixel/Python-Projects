# Expense Tracker
from functools import reduce

expense_list = []
# 1. Add Expense


class Expense:
    def __init__(self, expense_name, Amount, Category):
        self.expense_name = expense_name
        self.Amount = Amount
        self.Category = Category

    def all_Expense(self):
        print(
            f"Expense Name:{self.expense_name} \nAmount:{self.Amount}.\n Category:{self.Category}")


def view_all_Expense():
    for item in expense_list:
        item.all_Expense()


def search_category():
    catagoryTo_search = input("Enter which catagory do you want to Search:")
    found = False
    for item in expense_list:
        if item.Category == catagoryTo_search:
            item.all_Expense()
            found = True
    if found == False:
        print("This Category Does not Exist.")

# Add Expense


def add_expence():
    while True:
        try:
            expence_name = input("Enter the name of Expense:")
            amount = int(input("Enter the Amount you Spent:"))
            if amount < 0:
                print("Enter Poitive Expense! Do you Count money in negative? :)")
                continue
            category = input("Enter the Category of Expense:")
            new_expence = Expense(expence_name, amount, category)
            expense_list.append(new_expence)
            user = input("Wants to continue(y/n)? ")
            if user == 'n':
                print("thanks")
                break
        except ValueError as err:
            print(err)
        else:
            print("!!!Successfuly Added At Expense Tracker!!!")
        finally:
            print("Make all your Expense traking!")


# Total Expense

def total_func():
    total_list = []
    for item in expense_list:
        total_list.append(item.Amount)
    return total_list

# Higest expence


def highest_expense():
    bill = 0
    for high in expense_list:
        if high.Amount > bill:
            bill = high.Amount
            last = high

    last.all_Expense()


# Delete Expense


def delete_expense():
    found = False
    user = input("Enter the Expense you want to delete:")
    for item in expense_list:
        if user == item.expense_name:
            found = True
            expense_list.remove(item)
            break
    if found == False:
        print("The Expense is not present here.")
    else:
        print("!!Now This Expense no more exist in Your Expense Tracker!!")


# Menu
# @start
def menu():
    while True:
        try:
            print('''
            1.Add Expense
            2.View All Expenses
            3.Search Expenses by Category
            4.Calculate Total Spending
            5.Find Highest Expense
            6.Delete an Expense
            7.Exit''')
            choice = int(input("Enter as per the Manu Above: "))
            if choice == 1:
                add_expence()
            elif choice == 2:
                if len(expense_list) == 0:
                    print("!!Your Expense cart is Empty. So first fill that!!!")
                else:
                    view_all_Expense()
            elif choice == 3:
                if len(expense_list) == 0:
                    print("!!Your Expense cart is Empty so first fill that!!!")
                else:
                    search_category()
            elif choice == 4:
                collect = total_func()
                if len(collect) == 0:
                    print("!!!Your Expense cart is Empty so first fill that!!!")
                else:
                    total = reduce(lambda x, y: x+y, collect)
                    print(f"Total Expense: {total}rs.")
            elif choice == 5:
                if len(expense_list) == 0:
                    print("!!Your Expense cart is Empty so first fill that!!!")
                else:
                    highest_expense()
            elif choice == 6:
                if len(expense_list) == 0:
                    print("!!Your Expense cart is Empty so first fill that!!!")
                else:
                    delete_expense()
            elif choice == 7:
                break
            else:
                print("Invalid Input")
        except ValueError as err:
            print(err)
        else:
            print("Now you can Easily Maintain your Expense")


menu()
