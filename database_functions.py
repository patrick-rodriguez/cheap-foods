"""
Functions responsible for retrieving and updating prices of items
to/from the MySQL database to be displayed onto the user interface.
Author: Patrick Rodriguez
"""
import mysql.connector
from datetime import datetime

import Target_Scraper
import Safeway_Scraper
from Table_Class import Table

con = mysql.connector.connect(
    host='ix-dev.cs.uoregon.edu',
    port=3042,
    user='tnadeau',
    password='testpassword',
    database='Cheap_Staples'
)


def clear_date_table():
    """
    Clears the MySQL last_updated table.
    Returns: N/A
    """

    cursor = con.cursor()
    cursor.execute("DELETE FROM last_updated")  # MySQL query responsible for clearing table.
    con.commit()  # Commit MySQL query.
    


def update_last_updated():
    """
    Modifies the last_updated entry table responsible for indicating
    when the update() function was last ran by a user.
    Returns: N/A
    """

    cursor = con.cursor()
    unprocessed_date = datetime.today()  # Grab today's date.
    dt_string = unprocessed_date.strftime("%m/%d/%Y %H:%M:%S")  # String processing today's date.

    cursor.execute(f"insert into last_updated values ('{dt_string}')")  # MySQL query to update the entry.
    con.commit()  # Commit changes to table.
    


def get_last_updated():
    """
    Returns the date and time when the MySQL database was last updated.
    """

    cursor = con.cursor()
    cursor.execute("SELECT * FROM last_updated")  # MySQL query responsible for gathering date.
    return cursor.fetchall()[0]  # Returns date and time string.


def clear_safeway_table():
    """
    Clears all data in safeway MySQL database table.
    To be used when user updates prices.
    Returns: N/A
    """

    cursor = con.cursor()
    cursor.execute("DELETE FROM safeway")  # MySQL query to clear table.
    con.commit()  # Commit changes to MySQL.


def insert_to_safeway_table(item: str, price: float):
    """
    Inserts an item-price combination into the Fred Meyers MySQL database table.
    To be used when mass-updating the database table from scrapers.
    Returns: N/A
    """

    cursor = con.cursor()

    query = f"insert into safeway values('{item}', {price})"  # MySQL query that inserts values into database.
    cursor.execute(query)
    con.commit()  # Commit changes to MySQL database
    # Close connection to MySQL


def mass_insert_safeway_table(items: list):
    """
    Takes in a list of tuples that contain an item and corresponding price.
    For each tuple, function will call insert_to_safeway_table to insert
    into the MySQL database table.
    """
    for item_price_tuple in items:
        item = item_price_tuple[0].replace(r"'", r"\'")  # Addresses edge case of any apostrophes in item_name.
        price = item_price_tuple[1]
        insert_to_safeway_table(item, price)


def get_safeway_prices(item: str):
    """
    Used to gather item-price combination to be
    displayed to the user.
    """

    # Addressing edge cases in order to obtain the correct MySQL entries.
    if item == "Bread (White or wheat)":
        item = "Bread"
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

    cursor = con.cursor()

    # MySQL query responsible for obtaining appropriate information
    query = (f"SELECT *\n"
             f"FROM safeway\n"
             f"WHERE item_name LIKE '%{item}%'")

    cursor.execute(query)
    data = cursor.fetchall()  # Variable that contains appropriate data entries.

    return data[0][1]


def clear_target_table():
    """
    Clears all data in target MySQL database table.
    To be used when user updates prices.
    """

    cursor = con.cursor()
    cursor.execute("DELETE FROM target")  # MySQL query to clear target table.
    con.commit()  # Commit changes to MySQL database.


def insert_to_target_table(item: str, price: float):
    """
    Inserts an item-price combination into the Fred Meyers MySQL database table.
    To be used when mass-updating the database table.
    """
    # Edge case to avoid getting "tomato" and "tomato ketchup" when gathering price of tomato.
    if item == "Roma Tomato":
        item = "Roma Tomatoes"

    cursor = con.cursor()

    query = f"insert into target values('{item}', {price})"  # MySQL query that inserts values into database.
    cursor.execute(query)
    con.commit()  # Commit changes to MySQL database


def mass_insert_target_table(items: list):
    """
    Takes in a list of tuples that contain an item and corresponding price.
    For each tuple, function will call insert_to_target_table to insert
    into the MySQL database table.
    """
    for item_price_tuple in items:
        item = item_price_tuple[0].replace(r"'", r"\'")  # Addresses edge case of any apostrophes in item_name.
        price = item_price_tuple[1]
        insert_to_target_table(item, price)  # Insert entry to MySQL database.


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
    if item == "Bread (White or wheat)":
        item = "Bread"

    cursor = con.cursor()

    # MySQL query to obtain necessary data entries.
    query = (f"SELECT *\n"
             f"FROM target\n"
             f"WHERE item_name LIKE '%{item}%'")

    # Edge case with butter vs peanut butter.
    if item == "Butter":
        query = (f"SELECT *\n"
                 f"FROM target\n"
                 f"WHERE item_name = 'Butter'")

    cursor.execute(query)
    data = cursor.fetchall()  # Variable contains all necessary data entries.

    return data[0][1]


def update_prices():
    """
    The function to be called by the update button. It will clear and repopulate MySQL tables
    by running the scraper and calling functions to insert data into necessary tables.
    """

    # Clear MySQL tables
    clear_target_table()
    clear_safeway_table()
    clear_date_table()

    # Gathers updated prices by calling all scrapers.
    target_data = Target_Scraper.Target_Scrapper()
    safeway_data = Safeway_Scraper.scrape()

    # Insert the updated prices into the MySQL table.
    mass_insert_target_table(target_data)
    mass_insert_safeway_table(safeway_data)
    update_last_updated()


def format_and_display(items: list[str]):
    """
    Takes in a list of staples. First, it will run appropriate functions to retrieve
    appropriate prices from each grocery store. Then it will display and format the items and price
    combinations via a Table class object
    """
    # data list used to initialize a Table class object
    data = [("", "Safeway", "Target")]
    for item in items:
        # grab price of item from each grocery store.
        safeway_price = get_safeway_prices(item)
        target_price = get_target_prices(item)

        # format prices by (item, price#1, price#2) then append to data list.
        data.append((item, safeway_price, target_price))

    return Table(data)


def display_last_updated():
    return f"Last updated\n{get_last_updated()}"
