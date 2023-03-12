import mysql.connector


def clear_fredmeyers_table():
    """
    Clears all data in fredmeyers MySQL database table.
    To be used when user updates prices.
    """
    con = mysql.connector.connect(
        host='ix-dev.cs.uoregon.edu',
        port=3820,
        user='prodrig2',
        password='irodmario@2001',
        database='422project2'
    )

    cursor = con.cursor()
    cursor.execute("DELETE FROM fredmeyers")
    con.commit()
    con.close()


def insert_to_fredmeyers_table(item: str, price: float):
    """
    Inserts an item-price combination into the Fred Meyers MySQL database table.
    To be used when mass-updating the database table.
    """
    if item == "Roma Tomato":
        item = "Roma Tomatoes"

    # MySQL connection information
    con = mysql.connector.connect(
        host='ix-dev.cs.uoregon.edu',
        port=3820,
        user='prodrig2',
        password='irodmario@2001',
        database='422project2'
    )

    cursor = con.cursor()

    # MySQL query that inserts values into database.
    query = f"insert into fredmeyers values('{item}', {price})"
    cursor.execute(query)
    con.commit()
    con.close()


def mass_insert_fredmeyers_table(items: list):
    """
    Takes in a list of tuples that contain an item and corresponding price.
    For each tuple, function will call insert_to_fredmeyers_table to insert
    into the MySQL database table.
    """
    for item_price_tuple in items:
        item = item_price_tuple[0].replace(r"'", r"\'")
        price = item_price_tuple[1]
        insert_to_fredmeyers_table(item, price)


def update_fredmeyers_table(item: str, price: float):
    """
    To be called by the user to adjust any incorrect prices.
    """
    con = mysql.connector.connect(
        host='ix-dev.cs.uoregon.edu',
        port=3820,
        user='prodrig2',
        password='irodmario@2001',
        database='422project2'
    )

    cursor = con.cursor()
    query = (f"UPDATE fredmeyers\n"
             f"SET price = {price}\n"
             f"WHERE item_name = '{item}'")

    cursor.execute(query)
    con.commit()
    con.close()


def get_fredmeyers_prices(item: str):
    """
    Used to gather item-price combination to be
    displayed to the user.
    """
    con = mysql.connector.connect(
        host='ix-dev.cs.uoregon.edu',
        port=3820,
        user='prodrig2',
        password='irodmario@2001',
        database='422project2'
    )

    cursor = con.cursor()

    query = (f"SELECT *\n"
             f"FROM fredmeyers\n"
             f"WHERE item_name LIKE '%{item}%'")

    cursor.execute(query)
    data = cursor.fetchall()
    con.close()

    return data
