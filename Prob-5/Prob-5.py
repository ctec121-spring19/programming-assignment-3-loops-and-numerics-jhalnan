# Module 2
#   Programming Assignment 3
#     Prob-5.py

# Joel Halnan


def main():
    # variable definition
    pizzaCost = float(2.00)
    drinkCost = float(1.50)
    donutCost = float(0.56)

    pizzaQty = 2
    drinkQty = 1
    donutQty = 2

    subtotal = ((pizzaCost * pizzaQty) + (drinkCost * drinkQty) + (donutCost * donutQty))

    tax = (subtotal * .084)

    print()
    print("Receipt of Sale")
    print()
    #Itemized list section
    print("Pizza\tQTY:", pizzaQty, "\t\t", "$", "{:.2f}".format(pizzaCost * pizzaQty))
    print("Drink\tQTY:", drinkQty, "\t\t", "$", "{:.2f}".format(drinkCost * drinkQty))
    print("Donut\tQTY:", donutQty, "\t\t", "$", "{:.2f}".format(donutCost * donutQty))
    print("".center(35, "-"))
    #Subtotal, tax, and total section
    print("Subtotal:\t\t $", subtotal)
    print("Tax:\t\t\t $", "{:.2f}".format(tax))
    print()
    print("Total:\t\t\t $", "{:.2f}".format(tax + subtotal))
    print("".center(35,"-"))
    print()
    #User interface and change calculation section
    tendered = eval(input ("Enter amount paid:\t $ "))
    print()
    print("Amount tendered:\t $", "{:.2f}".format(tendered))
    print("Change:\t\t\t $", "{:.2f}".format(tendered - tax - subtotal))

main()