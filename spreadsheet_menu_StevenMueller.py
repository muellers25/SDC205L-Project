from datetime import datetime

print("stemue8520 Spreadsheet Automation Menu")
print("Choose a number from the following options")
print("1. Input Data")
print("2. View Current Data")
print("3. Generate Report")

# Next line retrieves the inputted option and stores it into the variable called selection.
selection = input("Enter your selection: ")

print(f"You selected {selection} at {datetime.now()}")
