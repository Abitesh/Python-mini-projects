import json
import os
import uuid
from datetime import datetime

DATA_FILE = os.path.join('.','Modules','expenses.json')
#if you cannot know the directory then use the below code
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DATA_FILE = os.path.join(BASE_DIR, '..', 'module', 'expenses.json')


def load_expenses():
    if not os.path.exists(DATA_FILE):
        print("The path file does not exits")
        return {}
    with open(DATA_FILE,'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError:
            return {}

def save_expense(data):
    directory = os.path.dirname(DATA_FILE)
    if directory and not os.path.exists(directory):
        print("The directory does not exit so i manually create one ")
        os.makedirs(directory)

    with open(DATA_FILE,'w') as file:
        json.dump(data,file,indent=4)


def Add_expense():
    expense_id = str(uuid.uuid4())[:8]
    date = datetime.today().strftime("%d-%m-%y")
    category = input("Enter the category of item: ")
    amount = float(input("Enter the Cost of the item: "))
    description = input("say aboutt the item: ")
    new_expense = {
        "id": expense_id,
        "date": date,
        "category": category,
        "amount": amount,
        "description" : description
    }
    return new_expense
    


def view_expense(data):
    if not data:
        print("No expense in the file")
        return
    
    for expense_id,details in data.items():
        print("ID: ",expense_id)
        print("Date: ",details["date"])
        print("Amount: ",details["amount"])
        print("description: ",details["description"])
        print()




def main():
    print("welcome to the Expenses TrackerCLI  ")
    Expenses = load_expenses()

    while True:
        print("\nCommands [add] , [view] , [exit]")
        cmd = input().strip().lower()
        if cmd=="add" :
            new_expense = Add_expense()
            Expenses[new_expense["id"]]=new_expense
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