"""
Table.py class header file

Contains the Table() class declaration & methods for easier formatting for display page module

"""


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
