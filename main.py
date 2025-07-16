from portfolio import add_stock_value, del_stock_value, view_stock_profile

while True:
    print("\n************* MENU ***********")
    print("1. Add stock\n2. Delete stock\n3. Display stock\n4. Exit")
    
    try:
        option = int(input("Enter your option: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if option == 1:
        print("\n***** Adding stock *****")
        try:
            amount = float(input("Enter amount you want to add: "))
            symbol = input("Enter the symbol of respective stock: ").upper()
            add_stock_value(symbol, amount)
        except ValueError:
            print("Invalid amount!")

    elif option == 2:
        print("\n***** Deleting stock *****")
        symbol = input("Enter the symbol of respective stock: ").upper()
        del_stock_value(symbol)

    elif option == 3:
        view_stock_profile()

    elif option == 4:
        print("\nSee you soon!")
        break

    else:
        print("Invalid Option!")
