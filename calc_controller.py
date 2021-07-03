class Controller:

    def __init__(self, calc):
        self.calc = calc
        self.window = None

    def set_view(self, window):
        self.window = window

    @staticmethod
    def input_number(num=1):
        num = 'первое' if num == 1 else 'второе'
        while True:
            number = input('Введите ' + num + ' число: ')
            try:
                number = int(number)
                break
            except ValueError:
                try:
                    number = float(number)
                    break
                except ValueError:
                    print('Вы ввели некорректное число. Попробуйте ещё раз!')
        return number

    def calc_add(self):
        print('Введите значения для расчёта суммы:')
        a = self.input_number()
        b = self.input_number(2)
        self.calc.add(a, b)
