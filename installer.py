import os   # OS comes default w/ Python standard library


def main():
    """
    Installer function:
    
    Installs python libraries:
        customtkinter
        bs4 (Beautiful Soup 4)
        mysql-connector-python

    
    """
    ########################## TRY PIP FIRST ##########################
    # Install tkinter
    os.system("pip install customtkinter")

    # Install Scraping Libraries
    os.system("pip install bs4")
    os.system("pip install requests")

    # Install Database Libraries
    os.system("pip install mysql-connector-python")


    ########################## TRY PIP3 IF PIP DIDN'T WORK ##########################
    # Install tkinter
    os.system("pip3 install customtkinter")

    # Install Scraping Libraries
    os.system("pip3 install bs4")
    os.system("pip3 install requests")

    # Install Database Libraries
    os.system("pip3 install mysql-connector-python")




if __name__ == "__main__":
    main()