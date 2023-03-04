"""
CHEAP STAPLES PROJECT   - CS 422 (3/4/2023)


Authors of Project:
    Jan Bermudez
    Garret Bunkers
    Dylan Hopper
    Timothy Nadeau
    Patrick Rodriguez

Description:
    This is the main file for all of CHEAP STAPLES.
    Run this file to execute the program.

"""

from Table_Class import Table



def main():
    """
    This is the Main function for the program, will call the user
    

    Variable Types:
        user_input  -   List of staples to find in database
        food_table  -   Table from Table_Class
    """
    print("hello world")

    ##################### MAIN FUNCTION #####################
    # Call UI
    user_input = 0 #getUserInput() # from UI.py
        # Input: User's input
        # Output: a list of strings to find ["milk", "eggs", "bacon"]



    # Give UI Input to Processing & Take Output from Processing
    food_table = 0 #processData(user_input)
        # Input: a list of strings to find ["milk", "eggs", "bacon"]
        # Output: A formatted table ready to visualize



    # Visualize Data
    # visualizeTable(food_table)
        # Input: A formatted table ready to visualize
        # Output: On screen



    ##################### TESTING #####################
    test_input = [("", "Winco", "Walmart"), ("Milk", "4.95", "6.07"), ("Eggs", "5.43", "3.49")]
    test_table = Table(test_input)





if __name__ == "__main__":
    main()