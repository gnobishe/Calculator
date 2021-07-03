class Window:

    def __init__(self, model, control):
        self.model = model
        self.control = control
        self.control.set_view(self)

    def print_result(self):
        self.control.calc_add()
        print(f'Результат сложения: {self.model.result}')
