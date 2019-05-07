"""
list_temp.py

This file takes in a list of degrees Farenheit from the user and returns
degrees Celcius.

"""

import sys

def conToCelc(faren):
    """
    converts farenheit to celcius
    """
    return (faren - 32)*(5/9)

list_faren = []  # empty list

while True:
    
    try:
        temp = input("Enter degrees Farenheit to convert to \
Celcius (or e to Exit): ")
    except EOFError:
        sys.exit(0)                

    if temp == 'e':
        break
    
    try:
        type(float(temp)) == float
    except ValueError:
        print("Not a number!")
        continue

    list_faren.append(float(temp))

list_faren.sort()  #put numbers into ascending order

"""
the following could probably use better formatting to handle large
numbers
"""

for i, temp in enumerate(list_faren[:]):  
    print(f"{list_faren[i]:10.2f}\u00b0F    ==> \
{conToCelc(temp):10.2f}\u00b0C")

sys.exit(0)
    




