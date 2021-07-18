import tkinter as tk


class View:
    """Class View simulates the interface that receives and sends data."""

    def __init__(self, model, control):

        # Connect the model and the controller.
        self.model = model
        self.control = control
        self.control.set_view(self)

        # Create and start GUI.
        self.__window = tk.Tk()
        self.create_calc()
        self.start_calc()

    def create_calc(self):
        """Create and arrange widgets."""

        self.__window.title('Калькулятор')
        self.__window.resizable(False, False)

        # Create output field.
        self.__result = tk.StringVar(self.__window)
        self.result = '0'
        self._label = tk.Label(self.__window, textvariable=self.__result, font='Arial 15', anchor=tk.E, padx=5, pady=5)
        self._label.grid(row=0, column=0, columnspan=3, sticky='we', padx=2, pady=2)

        # Create number buttons.
        for button in range(9):
            CalcButton(self, self.__window, text=button + 1, row=2 - button // 3 + 1, column=button % 3)
        CalcButton(self, self.__window, text=0, row=4, column=0)

        # Create operation buttons.
        CalcButton(self, self.__window, text='+', row=4, column=1)
        CalcButton(self, self.__window, text='=', row=4, column=2)

    def start_calc(self):
        """Start GUI."""

        self.__window.mainloop()

    @property
    def result(self):
        """Return a result value"""

        return self.__result.get()

    @result.setter
    def result(self, text):
        """Set a result value."""

        self.__result.set(text)


class CalcButton(tk.Button):
    """Create a button with set parameters."""

    def __init__(self, view, master, text, row, column, *args, **kwargs):

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

        # Set command.
        self['command'] = view.control.set_command(str(text))
