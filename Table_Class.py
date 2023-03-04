"""
Table.py class header file

Contains the Table() class declaration & methods for easier formatting for display page module

"""

from tkinter import *

# Declare some default table format settings
CELL_WIDTH = 13# int
FONT_SIZE = 20
FONT = "Arial"  # str


class Table():
    """
    Desc:
        Table class for processing to format found data on the database and pass to the 
        display module in order to visualize onto the screen.

        Formatting the data in this class will make it easier for the Display Page module to work with


    Parameters:
        self.rows  (int)            =   # of rows the table has (len of self.data)
        self.cols  (int)            =   # of cols the table has (len of tuples in self.data)
        self.data  (List[Tuples])   =   List of all the data to go in each cell (list of tuples)

        
    Methods:
        __init__()      -   Initalization function
    
    """


    def __init__(self, items:list):
        """
        Desc:
            Initalization function for table class

        Parameters:
            items   (List of Tuples)    - List of tuples where each tuple is a row, 
                                          and every item within the tuple is the value
                                          for each cell's column within that row.
                Example:
                    items = [("", "Winco", "Walmart"), ("Milk", "4.95", "6.07"), ("Eggs", "5.43", "3.49")]

                            Corresponds to this table:

                                    | Winco     | Walmart    
                            -----------------------------
                            Milk    | 4.95      | 6.07       
                            Eggs    | 5.43      | 3.49      
    

        Note:
            The 1st item (or 0th element) in "items" should be labels for the columns of the table

            If a cell needs to be empty, pass in an empty string

        """
        self.rows = len(items)
        self.cols = len(items[0])
        self.data = items
        self.e = 0

        # Set default table settings
        self.font = FONT
        self.font_size = FONT_SIZE
        self.cell_width = CELL_WIDTH


    def __str__(self):
        """
        Prints the table's data and rows/cols (for debugging)
        """
        return f"""Table list: {self.data}\nRows: {self.rows}\nCols: {self.cols}"""


    def setTableFormat(self, font: int = -1, font_size: int =  -1, cell_width = -1):
        """
        Desc:
            Change the style and formatting of the table.
            Options include:
                Font
                Font Size
                Cell Width

            If in your call to this method, you do not provide a certain parameter, the
                parameter will stay what it currently is
            
        Parameters:
            font        (str) - Name of font
            font_size   (int) - Size of font
            cell_width  (int) - Width of cell

        Returns:
            None
    
        """
        if font != -1:          # if font specified, apply font
            self.font = font

        if font_size != -1:     # if font size specified, apply font size
            self.font_size = font_size

        if cell_width != -1:    # if cell width specified, apply cell width
            self.cell_width = cell_width


    def visualizeTable(self):
        """
        Desc:
            Takes a given table, and displays it onscreen using tkinter

            Will declare a tkinter root, then use it to display
        
            NEEDS TKINTER TO WORK

        Parameters:
            None

        Returns:
            None
        """
        root = Tk()            # Declare a root
        for i in range(self.rows):  # For each row,
            for j in range(self.cols):  # then each column in the row,
                self.e = Entry(root, width=self.cell_width, font=(self.font, self.font_size))        # Init an entry      
                if (i == 0):                    # Make heading/1st row bold
                    self.e = Entry(root, width=self.cell_width, font=(self.font, self.font_size, 'bold')) 
                self.e.grid(row = i, column = j)     
                self.e.insert(END, self.data[i][j]) # insert value from self.data into table
        root.mainloop()        # Display on screen
