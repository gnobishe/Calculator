class Controller:
    """Class Controller simulates some functions to operate the calculator."""

    # Variables for creating commands.
    DIGITS = '0123456789'
    OPERATIONS = '+'
    RESULT = '='

    def __init__(self, model):

        # Connect the model and the view.
        self.model = model
        self.view = None

    def set_view(self, view):
        """Establish a connection between the view and the controller (because the view will be created a bit later."""

        self.view = view

    def digit_button(self, digit):
        """Create a command for a digit button."""

        if self.view.result == '0':
            self.view.result = digit
        else:
            self.view.result += digit

    def set_command(self, text):
        """Create a command."""

        if text in Controller.DIGITS:
            return lambda: self.digit_button(text)
        if text in Controller.OPERATIONS:
            pass
        if text == Controller.RESULT:
            pass
