import os   # OS comes default w/ Python standard library


def main():
    """
    Installer function:
    
    Installs python libraries:
        tkinter
        customtkinter
        bs4 (Beautiful Soup 4)
        selenium
        time

    
    """
    # Install tkinter
    os.system("pip install tkinter")
    os.system("pip install customtkinter")

    # Install Scraping Libraries
    os.system("pip install bs4")
    os.system("pip install selenium")
    os.system("pip install time")

    # Install Database Libraries


if __name__ == "__main__":
    main()