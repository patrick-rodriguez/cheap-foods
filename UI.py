import customtkinter
from tkinter import *
import Table_Class
import database_functions

# Staples is the list of all ingredients supported by Cheap Meals
staples = ["Milk (1gal)", 
            "Eggs",
            "Bread (White or wheat)",
            "Butter",
            "Ketchup",
            "Mustard",
            "Mayo",
            "Apples",
            "Corn",
            "Bananas",
            "Cream Cheese",
            "Peanut Butter",
            "Pinto Beans",
            "Black Beans",
            "White Rice",
            "Marinara Sauce",
            "Spaghetti",
            "Chicken Breasts",
            "Ground Beef",
            "Bacon",
            "Baking Soda",
            "Sugar (White Granulated)",
            "Flour (Enriched)",
            "Olive Oil",
            "Salt",
            "Pepper",
            "Oats",
            "Tomatoes",
            "Peanuts",
            "Ice cream",
]


# Class for the Scrollable Checkbox frame
class ScrollableCheckBoxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, item_list, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.checkbox_list = []
        for i, item in enumerate(item_list):
            self.add_item(item)

    def add_item(self, item):
        """
        Function creates a checkbox object for the item passed in
        and appends it to the checkbox_list
        """
        checkbox = customtkinter.CTkCheckBox(self, text=item)
        if self.command is not None:
            checkbox.configure(command=self.command)
        checkbox.grid(row=len(self.checkbox_list), column=0, padx=15, pady=10, sticky="w")
        self.checkbox_list.append(checkbox)

    def get_checked_items(self):
        """
        Returns current checked items in checkbox_list
        """
        return [checkbox.cget("text") for checkbox in self.checkbox_list if checkbox.get() == 1]


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Configure the main window
        customtkinter.set_appearance_mode("light")
        self.title("Cheap Meals")
        self.geometry("320x800")
        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)

        # Create scrollable checkbox frame
        self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(master=self, width=220, command=self.checkbox_frame_event,
                                                                 item_list=staples)
        # Position the checkbox frame
        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=15, pady=(55, 10), sticky="ns")

        # Create and Place "Cheap Meals" Label Title 
        cheap_meals_label = customtkinter.CTkLabel(master=self, text="Cheap Meals ®", font=("Helvetica", 26, "bold"))
        cheap_meals_label.place(relx=0.5, rely=0.04,anchor="center")

       #######################################################################################################################################

        # Create bottom frame for execution buttons
        self.buttons_frame = customtkinter.CTkFrame(master=self, width=200)
        # Position the button frame
        self.buttons_frame.grid(row=1, column=0, padx=15)

        # Create and Placae "View all" Button
        view_all_button = customtkinter.CTkButton(master=self.buttons_frame, text="View All", width=15, command=self.view_all_button_clicked)
        view_all_button.pack(padx=5, pady=10, side="left")

        # Create and Place "View Select" Button
        view_select_button = customtkinter.CTkButton(master=self.buttons_frame, text="View Select", width=15, command=self.view_select_button_clicked)
        view_select_button.pack(padx=5, pady=10, side="left")

        # Create and Place "Update Prices" Button
        update_prices_button = customtkinter.CTkButton(master=self.buttons_frame, text="Update Prices", width=15, command=self.update_prices_clicked)
        update_prices_button.pack(padx=5, pady=10, side="right")

        #######################################################################################################################################


    def checkbox_frame_event(self):
        """ 
        Function for debugging purposes.
        Prints the current checked items anytime the checkbox frame is checked or unchecked.
        """
        print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}")
    
    def view_all_button_clicked(self):
        """
        Function gets called when the user presses "View All" button.
        Passes entire staples list to format_and_display() from database_functions module.
        """
        print("view all was pressed")   # this is where database call happens for view all
        table = database_functions.format_and_display(staples)  
        table.setTableFormat()
        table.calcCellColours()
        table.visualizeTable()

    def view_select_button_clicked(self):
        """
        Function gets called when the user presses "View Select" button.
        Passes current checked items in scrollable_checkbox_frame to format_and_display()
        in the database_functions module.
        """
        if len(self.scrollable_checkbox_frame.get_checked_items()) == 0:
            print("You must select at least one item for view select.")
        else:
            selected_staples = self.scrollable_checkbox_frame.get_checked_items()
            table = database_functions.format_and_display(selected_staples)  
            table.setTableFormat()
            table.calcCellColours()
            table.visualizeTable()


    def update_prices_clicked(self):
        """
        Function gets called when the user presses "Update Prices" button.
        """
        database_functions.update_prices()
        # Create Popup window
        popup = customtkinter.CTk()
        popup.title("Cheap Meals")
        popup.geometry("210x80")

        # Create label and OK button for popup window
        label = customtkinter.CTkLabel(master=popup, text='Prices Successfully Updated!',
                                       pady=15, padx=10, font=("Helvetica", 16))
        OK_button = customtkinter.CTkButton(master=popup, text="Ok", width=15, command=popup.destroy)

        # Place label and button in popup window
        label.pack()
        OK_button.pack(pady=5)
        
        popup.mainloop()
