total_bill = 0  # Initialize the total bill

#  set up a loop to always prompt for new orders until the client declines
while True:
    print("Thank you for choosing Python Pizza Deliveries!")

    Bill = 0

    size = input("What size pizza do you want? S, M, or L?\n")
    if size == "S":
        Bill += 15
        print(f"The cost of the pizza is ${Bill}")
        add_pepperoni = input("Do you want pepperoni? Y or N\n")
        if add_pepperoni == "Y":
            Bill += 2
            print(f"Bill is at {Bill}")
    elif size == "M":
        Bill += 20
        print("The cost of the Pizza is $20")
        add_pepperoni = input("Do you want pepperoni? Y or N\n")
        if add_pepperoni == "Y":
            Bill += 3
    elif size == "L":
        Bill += 25
        print("The cost of the Pizza is $25")
        add_pepperoni = input("Do you want pepperoni? Y or N\n")
        if add_pepperoni == "Y":
            Bill += 3
    extra_cheese = input("Do you want extra cheese? Y or N\n")
    if extra_cheese == "Y":
            Bill += 1

    total_bill += Bill  # Add the current order's bill to the total

    print(f"Your total bill for this order is ${Bill}.")
    print(f"Your cumulative total is ${total_bill}.")

    another_order = input("Do you want to place another order? Y or N\n")
    if another_order != "Y":
        print("Thank you for choosing Python Pizza Deliveries! See you soon")
        break

print(f"Thank you for choosing Python Pizza Deliveries! Your final total bill is ${total_bill}.")
