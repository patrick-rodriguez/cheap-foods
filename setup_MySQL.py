"""
Script responsible for setting up Cheap Foods MySQL Database
and table population upon creation.
Author: Patrick Rodriguez
"""
import mysql.connector
import database_functions


def get_mysql_login():
    """
    This function will prompt the user to enter their MySQL information.
    In the circumstance that the user enters wrong information,
    they will be prompted again.
    """
    global database
    host = input("Enter MySQL Host (Either ix-dev.cs.uoregon.edu or ix.cs.uoregon.edu): ")
    username = input("Enter MySQL Username: ")
    password = input("Enter MySQL Password: ")
    port = input("Enter MySQL Port: ")

    try:
        database = mysql.connector.connect(
            host=host,
            port=port,
            user=username,
            password=password
        )

    except (Exception,):
        print("Login failed.")
        get_mysql_login()

    return database


def create_schema(db):
    """Create the MySQL scheme responsible for holding the individual grocery store tables."""
    cursor = db.cursor()
    cursor.execute("DROP SCHEMA IF EXISTS Cheap_Staples ;")
    cursor.execute("CREATE SCHEMA `Cheap_Staples` ;")


def create_tables(db):
    """
    Create the tables necessary to hold item name-price combinations for each grocery store. 
    Last_updated table indicating when the update function button last was clicked by the user.
    """
    cursor = db.cursor()

    grocery_stores = ["safeway", "target"]
    for store in grocery_stores:
        cursor.execute(f"CREATE TABLE `Cheap_Staples`.`{store}` ("
                       f"`item_name` VARCHAR(200) NOT NULL, "
                       f"`price` INT(10) NOT NULL"
                       f");")

    cursor.execute(f"CREATE TABLE `Cheap_Staples`.`last_updated` ("
                   f"`date_last_modified` VARCHAR(200) NOT NULL "
                   f");")

def populate_tables():
    print("Populating tables. Please wait.")
    database_functions.update_prices()
    print("Populating tables finished!\nHave fun using Cheap Staples!")

def main():
    db = get_mysql_login()
    create_schema(db)
    create_tables(db)
    populate_tables()

if __name__ == "__main__":
    main()
