class Controller:
    """
    Класс Controller моделирует контроллер, т. е. реализует определённые функции для управления калькулятором (ввод
    значений и отправка данных в модель).
    """

    def __init__(self, model):
        """
        Метод инициализирует атрибуты:
        1) __model - модель калькулятора (класс Model);
        2) __view - вид калькулятора (класс View) - изначально None.
        """

        self.__model = model
        self.__view = None

    def set_view(self, view):
        """
        Присуждает переменной __view инициализированный экземпляр класса View.
        """

        self.__view = view

    @staticmethod
    def input_number(num=1):
        """
        Метод выполняет проверку корректности введённого числа.
        """

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
        """
        Метод выполняет ввод значений и отправляет их модели (вызывает соответствующий метод) для расчёта суммы.
        """

        print('Введите значения для расчёта суммы:')
        a = self.input_number()
        b = self.input_number(2)
        self.__model.add(a, b)
