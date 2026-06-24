from inventory import view_products


def low_stock_report():

    products = view_products()

    print("\n===== LOW STOCK REPORT =====")

    found = False

    for product in products:

        if product[2] < 10:

            print(
                f"ID:{product[0]} "
                f"Name:{product[1]} "
                f"Qty:{product[2]}"
            )

            found = True

    if not found:
        print("No low stock items found.")


def inventory_value_report():

    products = view_products()

    total_value = 0

    for product in products:

        quantity = product[2]
        price = product[3]

        total_value += quantity * price

    print(
        f"\nTotal Inventory Value = ₹{total_value}"
    )
