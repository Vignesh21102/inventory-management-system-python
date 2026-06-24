from database import connect_db


def add_product(name, quantity, price):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO products
        (name, quantity, price)
        VALUES (?, ?, ?)
        """,
        (name, quantity, price)
    )

    conn.commit()
    conn.close()

    print("✅ Product Added Successfully")


def view_products():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM products"
    )

    products = cursor.fetchall()

    conn.close()

    return products


def update_product(product_id, quantity):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE products
        SET quantity = ?
        WHERE id = ?
        """,
        (quantity, product_id)
    )

    conn.commit()
    conn.close()

    print("✅ Product Updated Successfully")


def delete_product(product_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM products
        WHERE id = ?
        """,
        (product_id,)
    )

    conn.commit()
    conn.close()

    print("✅ Product Deleted Successfully")


def search_product(name):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM products
        WHERE name LIKE ?
        """,
        (f"%{name}%",)
    )

    result = cursor.fetchall()

    conn.close()

    return result
