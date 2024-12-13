# Medication Management System

## Overview
Medication Management System is a Python-based application designed to manage a medication inventory. It supports functionalities such as listing medications, registering new entries, updating stock and prices, sorting by quantity, generating reports, and more.

## Features

1. **List Medications**
   - Displays all registered medications with details like description, code, quantity, and price.

2. **Register New Medications**
   - Add a new medication to the inventory, ensuring unique codes for each item.

3. **Sort Medications by Quantity**
   - Allows sorting in ascending or descending order based on quantity.

4. **Search Medications**
   - Search by description or code to find specific medications.

5. **Remove Medications**
   - Remove a medication from the inventory using its code.

6. **Check Out-of-Stock Medications**
   - Lists all medications with zero quantity.

7. **Filter by Low Quantity**
   - Identifies medications with quantities below a user-defined threshold.

8. **Update Stock**
   - Adjust the stock quantity for a specific medication (positive for addition, negative for subtraction).

9. **Update Price**
   - Modify the price of a specific medication, ensuring the new price is not lower than the current price.

10. **Calculate Total Stock Value**
    - Computes the total monetary value of all medications in stock.

11. **Calculate Estimated Profit**
    - Estimates potential profit based on cost calculations for each medication.

12. **Generate General Report**
    - Provides a detailed report of all medications, including total values and overall revenue.

## Installation
1. Clone the repository or download the source code.
2. Ensure you have Python 3 installed on your system.
3. Run the script in a Python environment to start managing the inventory.

## Usage
1. Run the script.
2. Use the interactive menu to select options.
3. Follow on-screen prompts to input data or perform actions.

## Interactive Menu Options
```
1. List medications
2. Register new medication
3. Sort medications by quantity
4. Search medication
5. Remove medication
6. Check out-of-stock medications
7. Filter by low quantity
8. Update stock
9. Update price
10. Calculate total stock value
11. Calculate estimated profit
12. General report
13. Exit
```

## Example
### Initial Medication Stock:
```python
initial_availability = "Ozempic;201;15;1200.00#Victoza;202;10;700.00#Trulicity;203;50;800.00#Byetta;204;40;500.00#Bydureon;205;10;550.00#Rybelsus;206;8;600.00#Metformin;207;30;100.00#Jardiance;208;25;400.00#Farxiga;209;5;450.00#Invokana;210;3;400.00#Amaryl;211;12;150.00#Glifage;212;7;100.00"
```
### Registering a New Medication:
```
Enter description: Aspirin
Enter code: 213
Enter quantity: 50
Enter price: 25.00
```
### Sample Report:
```
## General Medication Report ##
Description          Code      Quantity  Price     Total Value   
Ozempic              201       15        $1200.00   $18000.00
...
Total revenue: $XXXXX.XX
```

## Contribution
Feel free to contribute by submitting issues or pull requests.

## License
This project is licensed under the MIT License.
