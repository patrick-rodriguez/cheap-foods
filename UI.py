import customtkinter
import tkinter
import Table_Class


staples = ["Milk (1gal)", 
            "Eggs",
            "Bread (White or wheat)",
            "Staples",
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
            "Baking Powder",
            "Baking Soda",
            "Vanilla",
            "Sugar (White Granulated)",
            "Flour (Enriched)",
            "Olive Oil",
            "Salt",
            "Pepper",
            "Oats",
            "Tomatoes",
            "Peanuts",
            "Ice cream (vanilla)",
]


# class for left scrollable checkbox frame
class ScrollableCheckBoxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, item_list, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.checkbox_list = []
        for i, item in enumerate(item_list):
            self.add_item(item)

    def add_item(self, item):
        checkbox = customtkinter.CTkCheckBox(self, text=item)
        if self.command is not None:
            checkbox.configure(command=self.command)
        checkbox.grid(row=len(self.checkbox_list), column=0, padx=15, pady=10, sticky="w")
        self.checkbox_list.append(checkbox)

    def remove_item(self, item):
        for checkbox in self.checkbox_list:
            if item == checkbox.cget("text"):
                checkbox.destroy()
                self.checkbox_list.remove(checkbox)
                return

    def get_checked_items(self):
        return [checkbox.cget("text") for checkbox in self.checkbox_list if checkbox.get() == 1]


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Cheap Meals")
        self.geometry("320x500")
        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)

        # create scrollable checkbox frame
        self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(master=self, width=220, command=self.checkbox_frame_event,
                                                                 item_list=staples)
        # padx moves frame to the right, pady adds padding to the top AND bottom
        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=15, pady=(15, 10), sticky="ns")

       #######################################################################################################################################

        # Frame for Execution Buttons
        self.buttons_frame = customtkinter.CTkFrame(master=self, width=200)
        self.buttons_frame.grid(row=1, column=0, padx=15)

        # View all Button
        view_all_button = customtkinter.CTkButton(master=self.buttons_frame, text="View All", width=15, command=self.view_all_button_clicked)
        view_all_button.pack(padx=5, pady=10, side="left")

        # View select Button
        view_select_button = customtkinter.CTkButton(master=self.buttons_frame, text="View Select", width=15, command=self.view_select_button_clicked)
        view_select_button.pack(padx=5, pady=10, side="left")

        # Update Prices Button
        update_prices_button = customtkinter.CTkButton(master=self.buttons_frame, text="Update Prices", width=15, command=self.update_prices_clicked)
        update_prices_button.pack(padx=5, pady=10, side="right")

        #######################################################################################################################################

        # This frame is not in use at the moment, im looking for way to embed the table window into the master frame with the checkbox but for now,
        # we have a working visualizer
        self.table_frame = customtkinter.CTkScrollableFrame(master=self, width=900, height=500, bg_color="blue")
    

    def checkbox_frame_event(self):
        """ Function for debugging purposes """
        print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}")
    
    def view_all_button_clicked(self):
        print("view all was pressed")   # this is where database call happens for view all

    def view_select_button_clicked(self):
        if len(self.scrollable_checkbox_frame.get_checked_items()) == 0:
            print("You must select at least one item for view select.")
        else:
            print("view select was pressed")   # this is where database call to retrieve prices happens
            # these are temp dummy values
            selected_staples = [("", "Winco", "Walmart"), ("Milk", "4.95", "6.07"), ("Eggs", "5.43", "3.49"), ("Milk", "4.95", "6.07"), ("Milk", "4.95", "6.07"),
                ("Milk", "4.95", "6.07"), ("Milk", "4.95", "6.07"), ("Milk", "4.95", "6.07"), ("Milk", "4.95", "6.07"), ("Milk", "4.95", "6.07"),
                ("Milk", "4.95", "6.07"), ("Milk", "4.95", "6.07"), ("Milk", "4.95", "6.07"), ("Milk", "4.95", "6.07"), ("Milk", "4.95", "6.07"),
                ("Milk", "4.95", "6.07"), ("Milk", "4.95", "6.07"), ("Milk", "4.95", "6.07"), ("Milk", "4.95", "6.07"), ("Milk", "4.95", "6.07"),
                ("Milk", "4.95", "6.07"), ("Milk", "4.95", "6.07"), ("Milk", "4.95", "6.07"), ("Milk", "4.95", "6.07"), ("Milk", "4.95", "6.07")]
            table = Table_Class.Table(selected_staples)
            table.setTableFormat()
            table.calcCellColours()
            table.visualizeTable()

    def update_prices_clicked(self):
        print("refreshing price database")    # this is where call happens to refresh database prices
            

if __name__ == "__main__":
    customtkinter.set_appearance_mode("light")
    app = App()
    app.mainloop()
