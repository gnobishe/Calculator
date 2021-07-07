class Model:
    """
    Класс Model моделирует расчётные возможности калькулятора (функции, выполняющие расчёты).
    """

    def __init__(self):
        """
        Метод инициализирует атрибуты:
        1) __result - результат операций (начальное значение 0).
        """

        self.__result = 0

    @property
    def result(self):
        """
        Свойство-геттер позволяет получить значение результата операций.
        """

        return self.__result

    def add(self, a, b):
        """
        Метод вычисляет сумму двух чисел и записывает её в переменную.
        """

        self.__result = a + b
