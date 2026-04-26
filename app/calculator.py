import math


class BaseCalculator:
    Types = {}

    def __init_subclass__(cls, **kwargs):
        cls.Types[cls.Type] = cls

    @classmethod
    def factory(cls, calculator_type, *args, **kwargs):
        return cls.Types[calculator_type](*args, **kwargs)

    def add(self, a, b):
        raise NotImplementedError

    def subtract(self, a, b):
        raise NotImplementedError

    def multiply(self, a, b):
        raise NotImplementedError

    def divide(self, a, b):
        raise NotImplementedError


class SimpleCalculator(BaseCalculator):
    Type = "simple"

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


class SuperCalculator(BaseCalculator):
    Type = "super"

    def __init__(self):
        self.history = []

    def add(self, a, b):
        res = a + b
        self.history.append(res)
        return res

    def subtract(self, a, b):
        res = a - b
        self.history.append(res)
        return res

    def multiply(self, a, b):
        res = a * b
        self.history.append(res)
        return res

    def divide(self, a, b):
        res = a / b
        self.history.append(res)
        return res

    def power(self, a, b):
        res = a**b
        self.history.append(res)
        return res

    def sqrt(self, a):
        res = math.sqrt(a)
        self.history.append(res)
        return res

    # Known Bug
    def modulo(self, a, b):
        res = a + b
        self.history.append(res)
        return res

    # Not implemented yet
    def log(self, a):
        pass
