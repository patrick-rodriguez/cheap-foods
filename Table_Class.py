"""
Table.py class header file

Contains the Table() class declaration & methods for easier formatting for display page module

"""

from tkinter import *

# Declare some default table format settings
CELL_WIDTH = 13 # int
CELL_COLOUR = "white"   # str
FONT_SIZE = 12  # int
FONT = "Arial"  # str

    # Colour Winners
    # Green = "lawn green"
    # Red = "salmon"

class Table():
    """
    Desc:
        Table class for processing to format found data on the database and pass to the 
        display module in order to visualize onto the screen.

        Formatting the data in this class will make it easier for the Display Page module to work with


    Variables:
        self.rows  (int)                =   # of rows the table has (len of self.data)
        self.cols  (int)                =   # of cols the table has (len of tuples in self.data)
        self.data  (List[Tuples])       =   List of all the data to go in each cell (list of tuples)
        self.cell_colours (List[Tuples])=   List of tuples that record cell colour for each cell (list of tuples)

        Default Cell Value Variables    (when creating a table, the self.visualizeTable() method will use these values)
        self.font           (str)       =   Name of font
        self.font_size      (int)       =   Size of font
        self.cell_width     (int)       =   Width of cell
        self.cell_colour    (str)       =   Colour of cell

        
    Methods:
        __init__()      -   Initalization function
        __str__()       -   String form of the table (Prints some variables -- Used for debugging)
        setTableFormat()-   Adjust the style of the table: Font, Font Size, Cell Width, & Cell Colour
        calcCellColours() - Updates self.cell_colours : Goes through the data, and compares prices on each row,
                                will assign the cell w/ cheapest price a green background colour
        visualizeTable()-   Display the table on a seperate window
        
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
        self.rows = len(items)      # Table rows
        self.cols = len(items[0])   # Table cols
        self.data = items           # List of tuples of row data
        self.cell_colours = []      # List of tuples of cell colour data
        self.e = 0                  # Init for tkinter to graph

        # Set default table settings
        self.font = FONT                # Set default font
        self.font_size = FONT_SIZE      # Set default font size
        self.cell_width = CELL_WIDTH    # Set default cell width
        self.cell_colour = CELL_COLOUR  # Set default cell colour


    def __str__(self):
        """
        Prints the table's data and rows/cols (for debugging)
        """
        return f"""Table list: {self.data}\nColour list: {self.cell_colours}\nRows: {self.rows}\nCols: {self.cols}"""


    def setTableFormat(self, font = -1, font_size: int =  -1, cell_width: int = -1, cell_colour = -1):
        """
        Desc:
            Change the style and formatting of the table.
            Options include:
                Font
                Font Size
                Cell Width
                Cell Colour

            If in your call to this method, you do not provide a certain parameter, the
                parameter will stay what it currently is
            
        Parameters:
            font        (str) - Name of font
            font_size   (int) - Size of font
            cell_width  (int) - Width of cell
            cell_colour (str) - Colour of cell

        Returns:
            None        (but will update self.font, self.font_size, self.cell_width, self.cell_colour if specified)
    
        """
        if font != -1:          # if font specified, apply font
            self.font = font

        if font_size != -1:     # if font size specified, apply font size
            self.font_size = font_size

        if cell_width != -1:    # if cell width specified, apply cell width
            self.cell_width = cell_width

        if cell_colour != -1:   # if cell colour specified, apply cell colour
            self.cell_colour = cell_colour


    def calcCellColours(self):
        """
        Desc:
            Go through the table and for each row, calculate the cheapest value
                within the row, then assign that cell with a green colour
                (Essentialy inits self.cell_colours)

            All other cells will go off of the global default CELL_COLOUR variable (likely 'white')
                if not assigned a colour otherwise.

            MUST BECALLED PRIOR TO "self.visualizeGraph()" TO GET CELL_COLOURS INIT'D

        Parameters:
            None
        
        Returns:
            None    (but updates self.cell_colours)
        """
        # Chosen colour names
            # Green     = "lawn green"
            # Red       = "salmon"

        self.cell_colours = []  # Erase current list
        smallest = float('inf') # Declare outside of loop for memory purposes
        smallest_index = self.cols
        smallest_indexes = []   # Declare a list to keep track of the case where there could be many "cheapest" prices
        for i in range(self.rows):
            temp_row_colours = []           # Create a temp row colour list to append colours to before converting to a tuple
            smallest = 9999999              # Reset smallest number
            smallest_index = self.cols + 10 # Set smallest index to be > than cols so after done computing row, 
                                            # if it's still bigger than # of cols, there weren't any numbers in the row
            smallest_indexes = []           # Reset list of smallest indexes
            for j in range(self.cols):
                temp_row_colours.append(CELL_COLOUR)    # Set to default colour
                try:
                    temp_num = float(self.data[i][j])
                except:
                    continue    # Skip if it couldn't convert to number
            
                if temp_num < smallest:
                    # print(f"Found that {temp_num} < {smallest}, setting index to {smallest_index}")   # DEBUG
                    smallest = temp_num
                    smallest_index = j
                    smallest_indexes = [j]
                elif temp_num == smallest:
                    smallest_indexes.append(j)


            if smallest_index <= self.cols: # Since default smallest_index is > than cols, see if it found a small number thats not a string
                for z in range(len(smallest_indexes)):  # check if multiple smallest values
                    temp_row_colours[smallest_indexes[z]] = "lawn green" # Set smallest value to green
                
            temp_tuple = tuple(temp_row_colours)    # Convert temp row colour list to a tuple
            self.cell_colours.append(temp_tuple)    # Append the tuple to self.cell_colours buffer
            

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
        root.title("Safeway vs Target") # Set window title
        for i in range(self.rows):  # For each row,
            for j in range(self.cols):  # then each column in the row,
                self.e = Entry(root, width=self.cell_width, bg=self.cell_colours[i][j], font=(self.font, self.font_size))        # Init an entry      
                if (i == 0):                    # Make heading/1st row bold
                    self.e = Entry(root, width=self.cell_width, bg=self.cell_colours[i][j],font=(self.font, self.font_size, 'bold')) 
                self.e.grid(row = i, column = j)     
                self.e.insert(END, self.data[i][j]) # insert value from self.data into table
        root.mainloop()        # Display on screen
