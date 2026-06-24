from inventory import *
from reports import *

while True:

    print("\n========================")
    print(" INVENTORY MANAGEMENT ")
    print("========================")

    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Search Product")
    print("6. Low Stock Report")
    print("7. Invesntory Value")
    print("8. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":

        name = input("Product Name: ")

        quantity = int(
            input("Quantity: ")
        )

        price = float(
            input("Price: ")
        )

        add_product(
            name,
            quantity,
            price
        )

    elif choice == "2":

        products = view_products()

        print(
            "\nID | Name | Quantity | Price"
        )

        print("-" * 40)

        for product in products:

            print(
                f"{product[0]} | "
                f"{product[1]} | "
                f"{product[2]} | "
                f"{product[3]}"
            )

    elif choice == "3":

        product_id = int(
            input("Enter Product ID: ")
        )

        quantity = int(
            input("New Quantity: ")
        )

        update_product(
            product_id,
            quantity
        )

    elif choice == "4":

        product_id = int(
            input("Enter Product ID: ")
        )

        delete_product(product_id)

    elif choice == "5":

        name = input(
            "Enter Product Name: "
        )

        results = search_product(name)

        if results:

            for product in results:

                print(
                    f"{product[0]} | "
                    f"{product[1]} | "
                    f"{product[2]} | "
                    f"{product[3]}"
                )

        else:

            print(
                "Product Not Found"
            )

    elif choice == "6":

        low_stock_report()

    elif choice == "7":

        inventory_value_report()

    elif choice == "8":

        print("Exiting...")

        break

    else:

        print("Invalid Choice")
