from datetime import datetime


def convertData(temperatureF):
    return (temperatureF - 32) * 5 / 9


def getInput():
    numberEntries = int(input("How many entries are you inputting? "))

    for entry in range(numberEntries):
        entryDate = input("Enter a date: ")
        temperatureF = float(input(
            "Enter the highest temp in Fahrenheit for the inputted date: "
        ))

        # convertData takes a Fahrenheit number and returns its Celsius value.
        temperatureC = convertData(temperatureF)

        print(f"The following was saved at {datetime.now()}:")
        print(f"{entryDate},{temperatureF},{temperatureC}")


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

if selection == "1":
    getInput()
else:
    print("Error: The chosen functionality is not implemented yet")
