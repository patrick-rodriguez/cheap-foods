import mysql.connector
from datetime import datetime

import Target_Scraper
import FredMeyer_Scraper
from Table_Class import Table

def clear_date_table():
    con = mysql.connector.connect(
        host='ix-dev.cs.uoregon.edu',
        port=3820,
        user='prodrig2',
        password='irodmario@2001',
        database='422project2'
    )

    cursor = con.cursor()
    cursor.execute("DELETE FROM last_updated")
    con.commit()
    con.close()

def update_last_updated():
    con = mysql.connector.connect(
        host='ix-dev.cs.uoregon.edu',
        port=3820,
        user='prodrig2',
        password='irodmario@2001',
        database='422project2'
    )

    cursor = con.cursor()
    unprocessed_date = datetime.today()
    dt_string = unprocessed_date.strftime("%m/%d/%Y %H:%M:%S")

    cursor.execute(f"insert into last_updated values ('{dt_string}')")
    con.commit()
    con.close()

def get_last_updated():
    con = mysql.connector.connect(
        host='ix-dev.cs.uoregon.edu',
        port=3820,
        user='prodrig2',
        password='irodmario@2001',
        database='422project2'
    )

    cursor = con.cursor()
    cursor.execute("SELECT * FROM last_updated")
    return cursor.fetchall()[0][0]
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

    # Edge cases in order to obtain the correct MySQL entries.
    if item == "Milk (1gal)":
        item = "Milk"
    if item == "Butter":
        item = "Butter Sticks"
    if item == "Apples":
        item = "Apple"
    if item == "Bananas":
        item = "Banana"
    if item == "Marinara Sauce":
        item = "Marinara"
    if item == "Chicken Breasts":
        item = "Chicken Breast"
    if item == "Sugar (White Granulated)":
        item = "Sugar"
    if item == "Flour (Enriched)":
        item = "Flour"
    if item == "Salt":
        item = "Iodized Salt"

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

    if item =
    cursor.execute(query)
    data = cursor.fetchall()
    con.close()

    return data[0][1]


def clear_target_table():
    """
    Clears all data in target MySQL database table.
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
    cursor.execute("DELETE FROM target")
    con.commit()
    con.close()


def insert_to_target_table(item: str, price: float):
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
    query = f"insert into target values('{item}', {price})"
    cursor.execute(query)
    con.commit()
    con.close()


def mass_insert_target_table(items: list):
    """
    Takes in a list of tuples that contain an item and corresponding price.
    For each tuple, function will call insert_to_target_table to insert
    into the MySQL database table.
    """
    for item_price_tuple in items:
        item = item_price_tuple[0].replace(r"'", r"\'")
        price = item_price_tuple[1]
        insert_to_target_table(item, price)


def update_target_table(item: str, price: float):
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
    query = (f"UPDATE target\n"
             f"SET price = {price}\n"
             f"WHERE item_name = '{item}'")

    cursor.execute(query)
    con.commit()
    con.close()


def get_target_prices(item: str):
    """
    Used to gather item-price combination to be
    displayed to the user.
    """
    # Edge cases in order to obtain the correct MySQL entries.
    if item == "Milk (1gal)":
        item = "Milk"
    if item == "Apples":
        item = "Apple"
    if item == "Bananas":
        item = "Banana"
    if item == "Marinara Sauce":
        item = "Marinara"
    if item == "Chicken Breasts":
        item = "Chicken Breast"
    if item == "Sugar (White Granulated)":
        item = "Sugar"
    if item == "Flour (Enriched)":
        item = "Flour"
    if item == "Salt":
        item = "Iodized Salt"

    con = mysql.connector.connect(
        host='ix-dev.cs.uoregon.edu',
        port=3820,
        user='prodrig2',
        password='irodmario@2001',
        database='422project2'
    )

    cursor = con.cursor()

    query = (f"SELECT *\n"
             f"FROM target\n"
             f"WHERE item_name LIKE '%{item}%'")

    if item == "Butter":
        query = (f"SELECT *\n"
                 f"FROM fredmeyers\n"
                 f"WHERE item_name = 'Butter'")

    cursor.execute(query)
    data = cursor.fetchall()
    con.close()

    return data[0][1]

def update_prices():
    clear_target_table()
    clear_fredmeyers_table()
    clear_date_table()

    target_data = Target_Scraper.Target_Scrapper()
    fredmeyer_data = FredMeyer_Scraper.scrape()

    mass_insert_target_table(target_data)
    mass_insert_fredmeyers_table(fredmeyer_data)
    update_last_updated()

def format_and_display(items: list[str]):
    data = [("", "Fred Meyer", "Target")]
    for item in items:
        fredmeyers_price = get_fredmeyers_prices(item)
        target_price = get_target_prices(item)
        data.append((item, fredmeyers_price, target_price))

    return Table(data)

FredMeyer_Scraper.scrape()