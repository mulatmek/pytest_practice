import math


class BaseCalculator:
    """Base calculator contract and implementation registry."""

    registry = {}

    def __init_subclass__(cls, **kwargs):
        """Register subclasses by their declared calculator type."""
        cls.registry[cls.calculator_type] = cls

    @classmethod
    def factory(cls, calculator_type, *args, **kwargs):
        """Build a calculator instance by type key."""
        return cls.registry[calculator_type](*args, **kwargs)

    def add(self, a, b):
        """Return the sum of two numbers."""
        raise NotImplementedError

    def subtract(self, a, b):
        """Return the difference of two numbers."""
        raise NotImplementedError

    def multiply(self, a, b):
        """Return the product of two numbers."""
        raise NotImplementedError

    def divide(self, a, b):
        """Return the quotient of two numbers."""
        raise NotImplementedError


class SimpleCalculator(BaseCalculator):
    """Calculator with basic arithmetic operations."""

    calculator_type = "simple"

    def add(self, a, b):
        """Return the sum of two numbers."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of two numbers."""
        return a - b

    def multiply(self, a, b):
        """Return the product of two numbers."""
        return a * b

    def divide(self, a, b):
        """Return the quotient of two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


class SuperCalculator(BaseCalculator):
    """Calculator that tracks operation history and advanced operations."""

    calculator_type = "super"

    def __init__(self):
        """Initialize operation history."""
        self.history = []

    def add(self, a, b):
        """Return the sum and store it in history."""
        res = a + b
        self.history.append(res)
        return res

    def subtract(self, a, b):
        """Return the difference and store it in history."""
        res = a - b
        self.history.append(res)
        return res

    def multiply(self, a, b):
        """Return the product and store it in history."""
        res = a * b
        self.history.append(res)
        return res

    def divide(self, a, b):
        """Return the quotient and store it in history."""
        res = a / b
        self.history.append(res)
        return res

    def power(self, a, b):
        """Return a raised to the power b and store it in history."""
        res = a**b
        self.history.append(res)
        return res

    def sqrt(self, a):
        """Return the square root and store it in history."""
        res = math.sqrt(a)
        self.history.append(res)
        return res

    # FIXME: Incorrect implementation; modulo should use `a % b`.
    def modulo(self, a, b):
        """Return modulo result and store it in history."""
        res = a + b
        self.history.append(res)
        return res

    # TODO: Implement logarithm operation with domain validation.
    def log(self, a):
        """Compute a logarithm value and store it in history."""
        pass
