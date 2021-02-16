from tkinter import *
from food_calculator import *


class FoodCalculatorGUI:
    def __init__(self, root=Tk()):
        self.__current_row = 0

        self.root = root
        self.root.wm_title('Dog Food Calculator')

        self.food_calculator = None
        self.dog_weight = self.add_entry_selector_widget(root, 'Enter dog\'s weight', "55")
        self.cal_per_cup_food = self.add_entry_selector_widget(root, 'Enter calories per cup of food', "417")
        self.cal_per_treat = self.add_entry_selector_widget(root, 'Enter calories per training treat', "1")
        self.life_stage = self.add_drop_down_widget(root, "Select life stage", life_stage_RER_factor_dict.keys())
        self.add_button_widget(root, "Calculate", "lightblue", self.calculate_food)
        self.text_box = Text(root, width=50, height=6, wrap=WORD)
        self.text_box.grid(row=self.__current_row, columnspan=3, sticky=W)

    def add_button_widget(self, frame, name, color, action=None):
        """
        Add a button widget
        :param frame: parent frame
        :param name: name of the button
        :param action: action of the button
        :param color: color of the button
        :return: None
        """
        Button(frame, text=name, bg=color, command=action).grid(row=self.__current_row, columnspan=3)
        self.__current_row += 1

    def add_drop_down_widget(self, frame, name, enum_values):
        """
        Add a drop down menu widget
        :param frame: parent frame
        :param name: name of the button
        :param enum_values: options of the menu
        :return: string variable
        """
        string_var = StringVar()
        Label(frame, text=name + ':').grid(row=self.__current_row, column=0, sticky=W)
        OptionMenu(frame, string_var, *enum_values).grid(
            row=self.__current_row, column=1, sticky=W, pady=2)
        self.__current_row += 1
        return string_var

    def add_entry_selector_widget(self, frame, name, default_value):
        """
        Add an entry selector widget (text box + button)
        :param frame: parent frame
        :param name: name of the widget
        :param default_value: default value to display in the text box
        :return: string variable
        """
        string_var = StringVar()
        string_var.set(default_value)
        Label(frame, text=name + ':').grid(row=self.__current_row, column=0, sticky=W)
        Entry(frame, textvariable=string_var).grid(
            row=self.__current_row, column=1, sticky=W, pady=2)
        self.__current_row += 1
        return string_var

    def calculate_food(self):
        self.food_calculator = FoodCalculator(dog_weight=self.dog_weight.get(),
                                              food_calories_per_cup=self.cal_per_cup_food.get(),
                                              treat_calories_per_unit=self.cal_per_treat.get(),
                                              life_stage=self.life_stage.get())

        self.text_box.insert(END, "Daily caloric intake:\n")
        self.text_box.insert(END, f"Total calories = {round(self.food_calculator.total_calories)}\n")
        self.text_box.insert(END, f"Normal food calories = {round(self.food_calculator.food_calories)}\n")
        self.text_box.insert(END, f"Number of food cups = {round(self.food_calculator.food_quantity, 1)}\n")
        self.text_box.insert(END, f"Treat calories = {round(self.food_calculator.treat_calories)}\n")
        self.text_box.insert(END, f"Number of treats = {round(self.food_calculator.treat_quantity)}\n")

    def mainloop(self):
        """
        Run the main loop of the window
        :return: None
        """
        self.root.mainloop()


def main():
    """
    Run this main function if this script is called directly.
    :return: None
    """
    food_calculator_gui = FoodCalculatorGUI()
    food_calculator_gui.mainloop()


if __name__ == "__main__":
    main()

