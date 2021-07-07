import tkinter as tk


class View:
    """Class View simulates the interface that receives and sends data."""

    def __init__(self, model, control):

        # Connect the model and the controller.
        self.__model = model
        self.__control = control
        self.__control.set_view(self)

        # Create and start GUI.
        self.__window = tk.Tk()
        self.__label = None
        self.create_calc()
        self.start_calc()

    def create_calc(self):

        """Create and arrange widgets."""
        self.__window.title('Калькулятор')
        self.__window.resizable(False, False)

        # Create output field.
        self.__label = tk.Label(self.__window, text='0', font='Arial 15', anchor=tk.E, padx=5, pady=5)
        self.__label.grid(row=0, column=0, columnspan=3, sticky='we', padx=2, pady=2)

        # Create number buttons.
        for button in range(9):
            CalcButton(self.__window, text=button + 1, row=2 - button // 3 + 1, column=button % 3)
        CalcButton(self.__window, text=0, row=4, column=0)

        # Create operation buttons.
        CalcButton(self.__window, text='+', row=4, column=1)
        CalcButton(self.__window, text='=', row=4, column=2)

    def start_calc(self):
        """Start GUI."""

        self.__window.mainloop()


class CalcButton(tk.Button):
    """Create a button with set parameters."""

    def __init__(self, master, text, row, column, *args, **kwargs,):

        # Set constants.
        super().__init__(master, *args, **kwargs)
        self['font'] = 'Arial 15'
        self['width'] = 4
        self['padx'] = 5
        self['pady'] = 2
        self['relief'] = tk.GROOVE
        self['bg'] = 'white'
        self['activebackground'] = '#999388'
        self['borderwidth'] = 0

        # Set variables.
        self['text'] = text
        self.grid(row=row, column=column, padx=2, pady=2)
