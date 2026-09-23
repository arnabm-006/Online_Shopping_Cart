# Fixed product catalog stored as tuple of tuples
PRODUCTS = (
    (1, "Wireless Mouse", 550.0),
    (2, "Mechanical Keyboard", 1800.0),
    (3, "USB-C Cable", 250.0),
    (4, "Laptop Stand", 900.0)
)

cart = []  # List of tuples: [(item_name, unit_price, quantity), ...]

while True:
    print("\n--- ONLINE SHOPPING CART ---")
    print("1. View Available Products")
    print("2. Add Item to Cart")
    print("3. View Cart & Total")
    print("4. Remove Item from Cart")
    print("5. Checkout & Exit")
    
    choice = input("Enter your choice (1-5): ")

    # 1. VIEW CATALOG
    if choice == '1':
        print("\nID\tProduct Name\t\tPrice")
        print("-" * 40)
        for item in PRODUCTS:
            print(f"{item[0]}\t{item[1]:<20}\tRs.{item[2]:.2f}")

    # 2. ADD TO CART
    elif choice == '2':
        prod_id = int(input("Enter Product ID to buy: "))
        selected_product = None
        for item in PRODUCTS:
            if item[0] == prod_id:
                selected_product = item
                break
        
        if selected_product:
            quantity = int(input(f"Enter quantity for '{selected_product[1]}': "))
            if quantity > 0:
                # Store as a tuple in the cart list
                cart_item = (selected_product[1], selected_product[2], quantity)
                cart.append(cart_item)
                print(f"Added {quantity} x {selected_product[1]} to cart.")
            else:
                print("Quantity must be greater than 0.")
        else:
            print("Product ID not found.")

    # 3. VIEW CART
    elif choice == '3':
        if not cart:
            print("Your cart is empty.")
        else:
            print("\nItem Name\t\tPrice\tQty\tSubtotal")
            print("-" * 50)
            total = 0.0
            for item in cart:
                name, price, qty = item
                subtotal = price * qty
                total += subtotal
                print(f"{name:<20}\tRs.{price:.2f}\t{qty}\tRs.{subtotal:.2f}")
            print("-" * 50)
            print(f"Grand Total: Rs.{total:.2f}")

    # 4. REMOVE ITEM
    elif choice == '4':
        if not cart:
            print("Cart is empty.")
        else:
            item_name = input("Enter the name of the product to remove: ").strip()
            removed = False
            for item in cart:
                if item[0].lower() == item_name.lower():
                    cart.remove(item)
                    print(f"Removed '{item[0]}' from cart.")
                    removed = True
                    break
            if not removed:
                print("Item not found in your cart.")

    # 5. CHECKOUT
    elif choice == '5':
        if cart:
            print("\n--- FINAL INVOICE ---")
            total = sum(item[1] * item[2] for item in cart)
            for item in cart:
                print(f"{item[0]} x {item[2]} = Rs.{item[1] * item[2]:.2f}")
            print(f"Total Amount Payable: Rs.{total:.2f}")
            print("Order Placed Successfully! Thank you for shopping.")
        else:
            print("Cart was empty. Thank you for visiting!")
        break

    else:
        print("Invalid choice! Please select 1-5.")