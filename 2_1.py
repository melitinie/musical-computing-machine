import doctest


class Chair:
    def __init__(self, material: str, height: float):
        """
        :param material: Материал, из которого сделан стул
        :param height: Высота стула

        Примеры:
        >>> chair = Chair("дерево", 50)
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть описан буквами")
        self.material = material

        if not isinstance(height, (int, float)):
            raise TypeError("Высота должна быть описана цифрами")
        if height <= 0:
            raise ValueError("Высота должна быть неотрицательным числом")
        self.height = height

    def is_durable_chair(self) -> bool:
        """
        Функция, которая проверяет, прочен ли стул.

        :return: Является ли стул прочным

        Примеры:
        >>> chair = Chair("дерево", 50)
        >>> chair.is_durable_chair()
        """

    def sit_on_chair(self) -> str:
        """
        Функция, которая имитирует посадку на стул.
        :return: Описание действий (вы сели на стул)
        """


class Table:
    def __init__(self, material: str, width: float):
        """
        :param material: Материал, из которого изготовлен стол
        :param width: Ширина стола

        Примеры:
        >>> table = Table("дерево", 200)
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть описан буквами")
        self.material = material

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина должна быть описана цифрами")
        if width <= 0:
            raise ValueError("Ширина должна быть неотрицательным числом")
        self.width = width

        def can_fit_people(self, number_of_people: int) -> bool:
            """
            Метод, проверяющий, может ли стол вместить заданное количество человек.

            :param number_of_people: Количество человек
            :return: Может ли стол вместить заданное количество человек

            Примеры:
            >>> table = Table("дерево", 200)
            >>> table.can_fit_people(10)
            """
            return number_of_people <= self.width // 50 # Пусть на одного человека нужно 50 см

        def is_stable(self, legs: int) -> bool:
            """
            Проверка, является ли стол устойчивым.

            :param legs: Количество ножек
            :return: Является ли стол устойчивым

            Примеры:
            >>> table.is_stable(4)
            """
            return self.legs == 4 #Считаем стол стабильным, только если у него 4 ножки


class Sofa():
    def __init__(self, material: str, width: float, depth: float, height: float):
        """
        :param material: Материал, из которого сделан диван
        :param width: Ширина дивана
        :param depth: Глубина дивана
        :param height: Высота дивана
        """
        self.material = material
        self.width = width
        self.depth = depth
        self.height = height

    def get_material(self) -> str:
        """
        Узнать, из какого материала сделан диван
        :return: Материал дивана
        """
        return self.material

    def get_dimensions(self) -> str:
        """
        Узнать габариты дивана, а именно его ширину, глубину и высоту в сантиметрах
        :return: Ширина, глубина и высота дивана в сантиметрах
        """
        return f"Ширина: {self.width} см, Глубина: {self.depth} см, Высота: {self.height} см"


if __name__ == "__main__":
    doctest.testmod()

