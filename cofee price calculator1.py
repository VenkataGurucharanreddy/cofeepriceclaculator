print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+          Coffee Shop          +")
print("+          Welcome              +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We serve the following coffees:")
print(" 1. Espresso=100/-")
print(" 2. Americano=150/-")
print(" 3. Latte=250/-")
print(" 4. Cappuccino=350/-")
print(" 5. Macchiato=375/-")
print(" 6. Mocha=400/-")
print(" 7. Flat White=489/-")
print("----------------------------")

# Ask how many cups of coffee are being ordered
try:
    num_cups = int(input("How many cups of coffee are being ordered? "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

total_price = 0

for i in range(num_cups):
    print(f"\nOrder {i + 1}:")
    print("*******************************")
    price = 0
    coffee = input("What type of coffee would you like?select(1 to 7): ")

    if coffee == "1":
        price = 100
    elif coffee == "2":
        price = 150
    elif coffee == "3":
        price = 250
    elif coffee == "4":
        price = 350
    elif coffee == "5":
        price = 375
    elif coffee == "6":
        price = 400
    elif coffee == "7":
        price = 489
    else:
        print("Sorry, we don't serve that type of coffee.")
        continue
    print("-"*30)
    # Check if a valid coffee type was selected
    if price > 0:
        size = input("1.Medium\n 2.L\n 3.XL \n What size Would you like?(select 1 to 3): ")
        
        if size == "2":
            price += 10  # Extra charge for X size
        elif size == "3":
            price += 15  # Extra charge for XL size
        elif size == "1":
            pass  # No extra charge for Medium, it's the default
        else:
            print("Invalid size selected.")
            exit()  # Stop the program if an invalid size is entered
        print("-"*30)
        # Ask if they want to eat in or take away
        dining_option = input("1.Drink In \n2.Take Away \nWould you like to drink in or take away?select(1 or 2) :")
        
        if dining_option == "2":
            price += 20  # Extra charge for take-away
        elif dining_option == "1":
            pass  # No extra charge for eating in
        else:
            print("Invalid dining option selected.")
            exit()  # Stop the program if an invalid dining option is entered

        total_price += price


print("\n************ Receipt **********")
if total_price > 0:
    print("\n_____________________________")
    print(f"Total Bill for {num_cups} cup(s): {total_price:.2f}/-")

print("________________________________")
print("\nThank you ,visit again")
