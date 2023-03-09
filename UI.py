import customtkinter
import tkinter


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

# class ExecuteButtons(customtkinter.CTkFrame):
#     def __init__(self):
#         super().__init__()



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Cheap Meals")
        self.geometry("1200x800")
        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)

        # create scrollable checkbox frame
        self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(master=self, width=220, command=self.checkbox_frame_event,
                                                                 item_list=staples)
        # padx moves frame to the right, pady adds padding to the top AND bottom
        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=15, pady=15, sticky="ns")
        

        # self.view_all_button = customtkinter.CTkButton(master=self, text="View All")
        # self.view_all_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER,)

        # self.view_select_button = customtkinter.CTkButton(master=self, text="View Select")
        # self.view_select_button.place(relx=0.5, rely=0.5)

    def checkbox_frame_event(self):
        print(f"checkbox frame modified: {self.scrollable_checkbox_frame.get_checked_items()}")
    
    def button_function(self):
            print("view all was pressed")


    

if __name__ == "__main__":
    customtkinter.set_appearance_mode("light")
    app = App()
    app.mainloop()