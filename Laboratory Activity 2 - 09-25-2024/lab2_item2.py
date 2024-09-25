def calculate_discount():
    while True:
        try:
            purchase_amount = float(input("Enter the total purchase amount: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        print(f"Initial Purchase Amount: {purchase_amount:.2f}")

        if purchase_amount > 5000:
            discount = purchase_amount * 0.10  
        else:
            discount = purchase_amount * 0.05  

        final_price = purchase_amount - discount

        print(f"Discount: {discount:.2f}")
        print(f"Final Price: {final_price:.2f}")

        try_again = input("Do you want to try again? (yes/no): ").strip().lower()
        if try_again != 'yes':
            print("Thank you!")
            break

calculate_discount()
