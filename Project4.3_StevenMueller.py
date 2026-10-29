from datetime import datetime

filePath = r"C:\PythonFiles\ZooData.csv"


# Convert a Fahrenheit temperature to Celsius and return the result.
def convertData(temperatureF):
    return (temperatureF - 32) * 5 / 9


# Append a comma-separated string to the CSV file and report success.
def insertData(path, data):
    try:
        with open(path, "a") as csvfile:
            csvfile.write(data + "\n")
        return True
    except OSError as error:
        print(f"Error writing to the file: {error}")
        return False


# Display the file path and the contents of the CSV file.
def viewData(path):
    try:
        with open(path, "r") as csvfile:
            print(f"The file {path}")
            print(csvfile.read(), end="")
    except OSError as error:
        print(f"Error reading the file: {error}")


# Collect dates and temperatures, convert them, and save each entry.
def getInput():
    try:
        numberEntries = int(input("How many entries are you inputting? "))
        if numberEntries < 1:
            print("Please enter at least 1 entry.")
            return
    except ValueError:
        print("Error: Enter a whole number for the number of entries.")
        return

    for entry in range(numberEntries):
        try:
            entryDate = input("Enter a date: ")
            temperatureF = float(input(
                "Enter the highest temp in Fahrenheit for the inputted date: "
            ))

            # convertData accepts a Fahrenheit number and returns Celsius.
            temperatureC = convertData(temperatureF)

            data = f"{entryDate},{temperatureF},{temperatureC}"

            if insertData(filePath, data):
                print(f"The following data was saved at {datetime.now()}:")
                print(data)

        except ValueError:
            print("Error: Temperature must be a number. Entry was not saved.")


print("stemue8520 Spreadsheet Automation Menu")
print("Choose a number from the following options")

menuOptions = [
    "1. Input Data",
    "2. View Current Data",
    "3. Generate Report"
]

for menuOption in menuOptions:
    print(menuOption)

selection = input("Enter your selection: ")

if selection in ("1", "2", "3"):
    print(f"You selected {selection} at {datetime.now()}")

    if selection == "1":
        getInput()
    elif selection == "2":
        viewData(filePath)
    else:
        print("Error: The chosen functionality is not implemented yet")
else:
    print("Error: Invalid choice selected.")
