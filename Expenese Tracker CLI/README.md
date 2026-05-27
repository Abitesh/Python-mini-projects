# 💰 Expense Tracker CLI

A lightweight, terminal-based application to manage and track daily expenses. 

Built entirely with Python, this project demonstrates core software engineering principles including File I/O, Data Serialization (JSON), UUID generation, and command-line interface (CLI) state management.

## 🚀 Features

* **Add Expenses:** Quickly log new expenses. The system automatically tags each entry with a unique 8-character ID and the current date.
* **View History:** Read out your complete expense history in a clean, terminal-friendly format.
* **Persistent Local Storage:** Emulates a NoSQL document database structure by saving all data locally to a nested `expenses.json` file.
* **Auto-Directory Creation:** Bulletproof path routing ensures the application creates its necessary storage folders automatically if they don't exist.
* **Zero Dependencies:** Built purely with Python's standard library. No `pip install` required.

## 📂 Project Structure

```text
📦 Python-mini-projects
 ┣ 📂 Modules
 ┃ ┗ 📜 expenses.json       # Auto-generated database file
 ┗ 📂 Expense Tracker CLI
   ┣ 📜 expense_CLI.py      # Main application code
   ┗ 📜 README.md           # Project documentation

*🛠️ Prerequisites*
Python 3.x installed on your system.

💻 How to Run
Clone this repository or download the project files.

Open your terminal and navigate to the folder containing the python script:

Bash
    cd "Expense Tracker CLI"
Run the application:

Bash
    python expense_CLI.py
(Note: Depending on your system, you might need to use python3 instead of python)

🕹️ Usage Guide
Once the application is running, you will see a prompt with available commands:
Commands [add] , [view] , [exit]

Type add and press Enter to log a new expense. You will be prompted to enter the category, amount, and a brief description.
Type view to see a list of all recorded expenses.
Type exit to safely close the application.

**🔮 Future Enhancements (Coming Soon)**

Analytics: Calculate and display total spending for the month.
Delete Feature: Remove an expense entry using its unique ID.
Category Filtering: View expenses grouped by specific categories (e.g., Food, Transport).
Built as a fundamental exercise in backend logic and data structuring.

##Things i want to add in the future
In Add_expense(), you have:
amount = float(input("Enter the Cost of the item: "))
If a user accidentally types "twenty" or hits Enter without typing anything, the float() function throws a ValueError and the entire application crashes.
Fix: Use a while loop with a try-except block to force the user to enter a valid number.

```python
    while True:
        try:
            amount = float(input("Enter the Cost of the item: "))
            if amount < 0:
                print("Amount cannot be negative. Try again.")
                continue
            break # Breaks out of the while loop if conversion succeeds
        except ValueError:
            print("Invalid input! Please enter a numeric value (e.g., 15.50).")