import json
import os
from datetime import datetime

DATA_FILE = os.path.join('..','Modules','expenses.json')

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE,'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError:
            return {}

def save_expense(data):
    print()

def Add_expense(data):
    print()

def view_expense(data):
    print()



def main():
    print("welcome to the Expenses TrackerCLI  ")
    Expenses = load_expenses()

    while True:
        print("\nCommands [add] , [view] , [exit]")
        cmd = input().strip().lower()
        if cmd=="add" :
            Add_expense(Expenses)
            save_expense(Expenses)
            print("Expenses added succesfully")
        elif cmd == "view":
            view_expense(Expenses)
        elif cmd=="exit":
            print("Thanks for visitng - yeahh")
            break
        else:
            print("Invalid input")
    



if __name__ == "__main__":
    main()