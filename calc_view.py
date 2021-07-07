class View:
    """
    Класс View моделирует интерфейс, с помощью которого можно получить или отправить данные.
    """

    def __init__(self, model, control):
        """
        Метод инициализирует атрибуты:
        1) __model - модель калькулятора (класс Model);
        2) __control - контроллер калькулятора (класс Control).
        """

        self.__model = model
        self.__control = control
        self.__control.set_view(self)

    def print_result(self):
        """
        Метод выполняет вызов соответствующего метода в контроллере для расчёта сложения двух чисел, а потом выводит
        результат, хранящийся в модели.
        """
        self.__control.calc_add()
        print(f'Результат сложения: {self.__model.result}')
