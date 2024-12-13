# Initial stock availability: Students should copy and paste the following code block as a string at the beginning of the program to define the initial stock of medications.
initial_availability = "Ozempic;201;15;1200.00#Victoza;202;10;700.00#Trulicity;203;50;800.00#Byetta;204;40;500.00#Bydureon;205;10;550.00#Rybelsus;206;8;600.00#Metformin;207;30;100.00#Jardiance;208;25;400.00#Farxiga;209;5;450.00#Invokana;210;3;400.00#Amaryl;211;12;150.00#Glifage;212;7;100.00"

def convert_list(medications):
    medication_list = []
    items = medications.split('#')
    for item in items:
        medication_list.append(item.split(';'))
    return medication_list

medications = convert_list(initial_availability)

# Register new medications
def register_medication(medications):
    description = input('Enter description: ')
    code = input('Enter code: ')
    for medication in medications:
        if medication[1] == code:
            print(f"An item with this code already exists: {code}")
            return

    quantity = int(input('Enter quantity: '))
    price = float(input('Enter price: '))

    medications.append([description, code, quantity, price])

# List medications
def list_medications(medications):
    print('\n## Medication List ##')
    for medication in medications:
        print(f"Description: {medication[0]}, Code: {medication[1]}, Quantity: {medication[2]}, Price: ${float(medication[3]):.2f}")

# Sort medications by quantity
def sort_medications(medications, order='ascending'):
    if order == 'descending':
        for i in range(len(medications)):
            for j in range(i + 1, len(medications)):
                if int(medications[i][2]) < int(medications[j][2]):
                    medications[i], medications[j] = medications[j], medications[i]
    else:
        for i in range(len(medications)):
            for j in range(i + 1, len(medications)):
                if int(medications[i][2]) > int(medications[j][2]):
                    medications[i], medications[j] = medications[j], medications[i]

    print("Medications sorted by quantity:")
    for i in range(len(medications)):
        print(f"Code: {medications[i][1]}, Name: {medications[i][0]}, Quantity: {int(medications[i][2])}")

# Search for medications
def search_medication(medications, **kwargs):
    found = []
    for medication in medications:
        if kwargs.get('description') and kwargs['description'].lower() in medication[0].lower():
            found.append(medication)
        elif kwargs.get('code') and kwargs['code'] == medication[1]:
            found.append(medication)

    if found:
        print("\n## Medications Found ##")
        list_medications(found)
    else:
        print("\nNo medications found.")

# Remove a medication
def remove_medication(medications, code):
    for medication in medications:
        if medication[1] == code:
            medications.remove(medication)
            print(f"\nMedication with code {code} successfully removed.")
            return
    print(f"\nMedication with code {code} not found.")

# Check out-of-stock medications
def check_out_of_stock(medications):
    print("\n## Out-of-Stock Medications ##")
    out_of_stock = [med for med in medications if int(med[2]) == 0]
    if out_of_stock:
        list_medications(out_of_stock)
    else:
        print("No medications are out of stock.")

# Filter medications by low quantity
def filter_low_quantity(medications, limit=10):
    print(f"\n## Medications with quantity below {limit} ##")
    low_quantity = [med for med in medications if int(med[2]) < limit]
    if low_quantity:
        list_medications(low_quantity)
    else:
        print("No medications with low quantity.")

# Update medication stock
def update_stock(medications, code, quantity):
    for medication in medications:
        if medication[1] == code:
            new_quantity = int(medication[2]) + quantity
            if new_quantity < 0:
                print("Insufficient stock to complete the operation.")
                return
            medication[2] = new_quantity
            print(f"Stock of medication {medication[0]} updated to {new_quantity}.")
            return
    print(f"Medication with code {code} not found.")

# Update medication price
def update_price(medications, code, new_price):
    for medication in medications:
        if medication[1] == code:
            if new_price < float(medication[3]):
                print("The new price cannot be lower than the current price.")
                return
            medication[3] = new_price
            print(f"Price of medication {medication[0]} updated to ${new_price:.2f}.")
            return
    print(f"Medication with code {code} not found.")

# Calculate total stock value
def calculate_total_value(medications):
    total = sum(int(med[2]) * float(med[3]) for med in medications)
    print(f"\nTotal stock value: ${total:.2f}")

# Calculate estimated profit
def calculate_estimated_profit(medications):
    total_profit = 0
    for medication in medications:
        price = float(medication[3])
        quantity = int(medication[2])
        if price < 500:
            cost = price * 0.75
        elif 500 <= price <= 700:
            cost = price * 0.80
        else:
            cost = price * 0.85
        total_profit += (price - cost) * quantity
    print(f"\nTotal estimated profit: ${total_profit:.2f}")

# General medication report
def general_report(medications):
    print("\n## General Medication Report ##")
    print(f"{'Description'.ljust(20)}{'Code'.ljust(10)}{'Quantity'.ljust(10)}{'Price'.ljust(10)}{'Total Value'.ljust(15)}")
    total_value = 0
    for medication in medications:
        total_item_value = int(medication[2]) * float(medication[3])
        total_value += total_item_value
        print(f"{medication[0].ljust(20)}{medication[1].ljust(10)}{str(medication[2]).ljust(10)}${float(medication[3]):.2f}   ${total_item_value:.2f}")
    print(f"\nTotal revenue: ${total_value:.2f}")

# Interactive menu
def interactive_menu():
    while True:
        print("\n### Menu ###")
        print("1. List medications")
        print("2. Register new medication")
        print("3. Sort medications by quantity")
        print("4. Search medication")
        print("5. Remove medication")
        print("6. Check out-of-stock medications")
        print("7. Filter by low quantity")
        print("8. Update stock")
        print("9. Update price")
        print("10. Calculate total stock value")
        print("11. Calculate estimated profit")
        print("12. General report")
        print("13. Exit")
        option = input("Choose an option: ")

        if option == "1":
            list_medications(medications)
        elif option == "2":
            register_medication(medications)
        elif option == "3":
            order = input("Enter sorting order (ascending or descending): ")
            sort_medications(medications, order)
        elif option == "4":
            criterion = input("Search by (description/code): ").lower()
            if criterion == "description":
                description = input("Enter description: ")
                search_medication(medications, description=description)
            elif criterion == "code":
                code = input("Enter code: ")
                search_medication(medications, code=code)
        elif option == "5":
            code = input("Enter the code of the medication to be removed: ")
            remove_medication(medications, code)
        elif option == "6":
            check_out_of_stock(medications)
        elif option == "7":
            limit = int(input("Enter quantity limit (default 10): ") or 10)
            filter_low_quantity(medications, limit)
        elif option == "8":
            code = input("Enter medication code: ")
            quantity = int(input("Enter the quantity to update (positive for addition, negative for subtraction): "))
            update_stock(medications, code, quantity)
        elif option == "9":
            code = input("Enter medication code: ")
            new_price = float(input("Enter new price: "))
            update_price(medications, code, new_price)
        elif option == "10":
            calculate_total_value(medications)
        elif option == "11":
            calculate_estimated_profit(medications)
        elif option == "12":
            general_report(medications)
        elif option == "13":
            print("Exiting the system!")
            break
        else:
            print("Invalid option. Please try again.")

interactive_menu()
