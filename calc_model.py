class Calculator:
    def __init__(self):
        self.__result = None

    @property
    def result(self):
        return self.__result

    def add(self, a, b):
        self.__result = a + b
