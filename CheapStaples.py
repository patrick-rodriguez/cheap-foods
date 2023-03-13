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
import UI


def main():
    """
    This is the Main function for the program, when ran it will call UI.py to construct the App window and
    all its associated functionally.
    """
    app = UI.App()
    app.mainloop()


if __name__ == "__main__":
    main()
