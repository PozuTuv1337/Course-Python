class Book:
    """Базовый класс книги."""
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Атрибут 'name' нельзя изменять")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        raise AttributeError("Атрибут 'author' нельзя изменять")

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс бумажной книги."""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # Вызываем сеттер для проверки

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = value

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}, страниц: {self.pages}"

    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, "
                f"pages={self.pages!r})")


class AudioBook(Book):
    """Класс аудио книги."""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # Вызываем сеттер для проверки

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        value = float(value)
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительной")
        self._duration = value

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}, продолжительность: {self.duration} ч."

    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, "
                f"duration={self.duration!r})")
