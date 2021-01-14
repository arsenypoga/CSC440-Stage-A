"""
Written By: Arseny Poga
Course: CSC440
"""


class Arith:
    """Class implementing basic math operations"""

    def __init__(self):
        pass

    @staticmethod
    def add(x: float, y: float) -> float:
        """Adds two numbers

        Args:
            x (float): A numerical value
            y (float): A numerical value

        Returns:
            float: x + y


        >>> Arith.add(10, 80)
        90
        >>> Arith.add(-99, 568)
        469

        >>> Arith.add(0.005, 30.78)
        30.785
        """
        return x + y

    @staticmethod
    def sub(x: float, y: float) -> float:
        """Substracts two numbers

        Args:
            x (float): A numerical value
            y (float): A numrical value

        Returns:
            float: x - y


        >>> Arith.sub(80, 10)
        70
        >>> Arith.sub(-99, 568)
        -667

        >>> Arith.sub(20, 30.7)
        -10.7
        """
        return x - y
