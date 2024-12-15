import doctest


class Car:
    def __init__(self, brand: str, max_speed: float, current_speed: float = 0):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param brand: Марка автомобиля
        :param max_speed: Максимальная скорость автомобиля (км/ч)
        :param current_speed: Текущая скорость автомобиля (км/ч)

        Примеры:
        >>> car = Car("Tesla", 250, 0)  # Инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть строкой")
        if not isinstance(max_speed, (int, float)):
            raise TypeError("Максимальная скорость должна быть числом")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом")
        if not isinstance(current_speed, (int, float)):
            raise TypeError("Текущая скорость должна быть числом")
        if current_speed < 0:
            raise ValueError("Текущая скорость не может быть отрицательным числом")

        self.brand = brand
        self.max_speed = max_speed
        self.current_speed = current_speed

    def accelerate(self, new_speed: float) -> None:
        """
        Ускорить автомобиль до определенной скорости.

        :param new_speed: Целевая скорость для ускорения (км/ч)
        :raise ValueError: Если целевая скорость выше максимальной или меньше 0

        Примеры:
        >>> car = Car("Tesla", 250, 0)
        >>> car.accelerate(100)
        """
        ...

    def brake(self) -> None:
        """
        Замедлить автомобиль до полной остановки.

        Примеры:
        >>> car = Car("Tesla", 250, 100)
        >>> car.brake()
        """
        ...

    def get_current_speed(self) -> float:
        """
        Получить текущую скорость автомобиля.

        :return: Текущая скорость (км/ч)

        Примеры:
        >>> car = Car("Tesla", 250, 50)
        >>> car.get_current_speed()
        50
        """
        ...


class Tree:
    def __init__(self, species: str, age: int, height: float):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param species: Вид дерева (название)
        :param age: Возраст дерева (лет)
        :param height: Высота дерева (м)

        Примеры:
        >>> oak = Tree("Oak", 10, 2.5)  # Инициализация экземпляра класса
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой")
        if not isinstance(age, int):
            raise TypeError("Возраст дерева должен быть целым числом")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным числом")
        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть числом")
        if height < 0:
            raise ValueError("Высота дерева не может быть отрицательным числом")

        self.species = species
        self.age = age
        self.height = height

    def grow(self, increment: float) -> None:
        """
        Увеличить высоту дерева на заданную величину (м).

        :param increment: Значение, на которое увеличиваем высоту
        :raise ValueError: Если increment отрицательный

        Примеры:
        >>> oak = Tree("Oak", 10, 2.5)
        >>> oak.grow(0.5)
        """
        ...

    def produce_oxygen(self) -> float:
        """
        Создать некоторое количество кислорода.

        :return: Объем выработанного кислорода

        Примеры:
        >>> oak = Tree("Oak", 10, 2.5)
        >>> oak.produce_oxygen()
        10.0
        """
        ...

    def get_age(self) -> int:
        """
        Получить возраст дерева.

        :return: Возраст дерева (лет)

        Примеры:
        >>> oak = Tree("Oak", 10, 2.5)
        >>> oak.get_age()
        10
        """
        ...


class Phone:
    def __init__(self, brand: str, model: str, battery_capacity: int):
        """
        Создает объект "Телефон"

        :param brand: Производитель телефона
        :param model: Модель телефона
        :param battery_capacity: Емкость батареи (мАч)

        Примеры:
        >>> smartphone = Phone("Apple", "iPhone 20", 3000)
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд телефона должен быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель телефона должна быть строкой")
        if not isinstance(battery_capacity, int):
            raise TypeError("Емкость батареи должна быть целым числом")
        if battery_capacity <= 0:
            raise ValueError("Емкость батареи должна быть положительным числом")

        self.brand = brand
        self.model = model
        self.battery_capacity = battery_capacity

    def make_call(self, number: str) -> None:
        """
        Совершить звонок по указанному номеру.

        :param number: Номер телефона для звонка
        :raise ValueError: Если номер некорректен

        Примеры:
        >>> smartphone = Phone("Apple", "iPhone 20", 3000)
        >>> smartphone.make_call("+1234567890")
        """
        ...

    def send_message(self, number: str, message: str) -> None:
        """
        Отправить сообщение на указанный номер.

        :param number: Номер телефона получателя
        :param message: Текст сообщения
        :raise ValueError: Если номер или сообщение некорректны

        Примеры:
        >>> smartphone = Phone("Apple", "iPhone 20", 3000)
        >>> smartphone.send_message("+1234567890", "Hello!")
        """
        ...

    def check_battery_level(self) -> int:
        """
        Проверить уровень заряда батареи.

        :return: Уровень заряда батареи в процентах

        Примеры:
        >>> smartphone = Phone("Apple", "iPhone 20", 3000)
        >>> smartphone.check_battery_level()
        85
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
