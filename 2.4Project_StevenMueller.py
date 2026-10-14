from datetime import datetime

print("stemue8520 Spreadsheet Automation Menu")
print("Choose a number from the following options")

menuOptions = [
    "1. Input Data",
    "2. View Current Data",
    "3. Generate Report"
]

# Loop through the list and display each menu option.
for menuOption in menuOptions:
    print(menuOption)

# Retrieve the user's option and store it in selection.
selection = input("Enter your selection: ")

if selection in ("1", "2", "3"):
    print(f"You selected {selection} at {datetime.now()}")
else:
    print("Error: Invalid choice selected.")
