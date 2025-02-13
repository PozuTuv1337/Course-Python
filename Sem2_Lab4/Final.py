class Device:
    """
    Базовый класс электронных устройств

    Attributes:
        brand (str): Бренд устройства (неизменяемый)
        model (str): Модель устройства (неизменяемая)
        year (int): Год выпуска устройства (неизменяемый)
    """

    def __init__(self, brand: str, model: str, year: int) -> None:
        """
        Инициализирует новый объект устройства с проверками типов и допустимых значений

        Args:
            brand (str): Бренд устройства
            model (str): Модель устройства
            year (int): Год выпуска устройства. Должен быть положительным целым числом
        Raises:
            TypeError: Если типы аргументов не соответствуют ожидаемым
            ValueError: Если year не является положительным числом
        """
        if not isinstance(brand, str):
            raise TypeError("brand должен быть строкой")
        if not isinstance(model, str):
            raise TypeError("model должен быть строкой")
        if not isinstance(year, int) or year <= 0:
            raise ValueError("year должен быть положительным целым числом")

        self._brand: str = brand  # Приватный атрибут: бренд
        self._model: str = model  # Приватный атрибут: модель
        self._year: int = year  # Приватный атрибут: год выпуска
        self._is_on: bool = False  # Приватный атрибут для отслеживания включен ли девайс

    @property
    def brand(self) -> str:
        """
        Только для чтения: возвращает бренд устройства
        """
        return self._brand

    @property
    def model(self) -> str:
        """
        Только для чтения: возвращает модель устройства
        """
        return self._model

    @property
    def year(self) -> int:
        """
        Только для чтения: возвращает год выпуска устройства
        """
        return self._year

    def __str__(self) -> str:
        """
        Возвращает краткое описание устройства

        Returns:
            str: Строка с информацией о бренде, модели и годе выпуска
        """
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self) -> str:
        """
        Возвращает подробное описание устройства

        Returns:
            str: Подробная информация об устройстве.
        """
        return (f"Device(brand={self.brand!r}, model={self.model!r}, "
                f"year={self.year!r}, is_on={self._is_on!r})")

    def turn_on(self) -> None:
        """
        Включает устройство

        Если устройство уже включено, выводит соответствующее сообщение
        """
        if not self._is_on:
            self._is_on = True
            print(f"{self} включено.")
        else:
            print(f"{self} уже включено.")


class Smartphone(Device):
    """
    Дочерний класс. Смартфон

    Attributes:
        os (str): Операционная система смартфона (неизменяемая)
        sim_card_count (int): Количество поддерживаемых SIM-карт (неизменяемое, должно быть >= 1)
    """

    def __init__(self, brand: str, model: str, year: int, os: str, sim_card_count: int) -> None:
        """
        Инициализирует новый объект смартфона, расширяя функциональность базового класса Device

        Args:
            brand (str): Бренд смартфона
            model (str): Модель смартфона
            year (int): Год выпуска смартфона
            os (str): Операционная система смартфона
            sim_card_count (int): Количество поддерживаемых SIM-карт. Должно быть целым числом >= 1
        Raises:
            TypeError: Если os не является строкой или sim_card_count не является целым числом
            ValueError: Если sim_card_count меньше 1
        """
        super().__init__(brand, model, year)
        if not isinstance(os, str):
            raise TypeError("os должен быть строкой")
        if not isinstance(sim_card_count, int):
            raise TypeError("sim_card_count должен быть целым числом")
        if sim_card_count < 1:
            raise ValueError("sim_card_count должен быть >= 1")

        self._os: str = os  # Приватный атрибут: операционная система
        self._sim_card_count: int = sim_card_count  # Приватный атрибут: количество SIM-карт

    @property
    def os(self) -> str:
        """
        Только для чтения: возвращает операционную систему смартфона
        """
        return self._os

    @property
    def sim_card_count(self) -> int:
        """
        Только для чтения: возвращает количество поддерживаемых SIM-карт
        """
        return self._sim_card_count

    def __str__(self) -> str:
        """
        Возвращает краткое строковое представление смартфона, включая операционную систему

        Returns:
            str: Краткая информация о смартфоне
        """
        base_str: str = super().__str__()
        return f"{base_str}, ОС: {self.os}"

    def __repr__(self) -> str:
        """
        Возвращает подробное строковое представление смартфона, включая операционную систему и количество SIM-карт

        Returns:
            str: Подробная информация о смартфоне
        """
        return (f"Smartphone(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, "
                f"is_on={self._is_on!r}, os={self.os!r}, sim_card_count={self.sim_card_count!r})")

    def turn_on(self) -> None:
        """
        Перегруженный метод turn_on для смартфона

        Перегрузка данного метода обоснована тем, что при включении смартфона необходимо
        дополнительно инициализировать функции, связанные с мобильной связью (например, настройка сети)

        Returns:
            None
        """
        print("Инициализация мобильной сети...")
        # Вызов базового метода для обновления состояния включения
        super().turn_on()
        print("Смартфон готов к работе.")


if __name__ == "__main__":
    # Пример использования базового класса Device
    device: Device = Device("LG", "G5", 2016)
    print(device)
    print(repr(device))
    device.turn_on()

    print("\n---\n")

    # Пример использования дочернего класса Smartphone
    smartphone: Smartphone = Smartphone("Apple", "iPhone 17", 2025, "iOS", 1)
    print(smartphone)
    print(repr(smartphone))
    smartphone.turn_on()
