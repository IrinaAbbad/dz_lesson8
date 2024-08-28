class Discount:
    def __init__(self, description: str, discount_percent: float):  # Конструктор класса Discount, инициализирующий описание и процент скидки.
        self.description = description  # Присваиваем описание скидки атрибуту description.
        self.discount_percent = discount_percent  # Присваиваем процент скидки атрибуту discount_percent.

    def apply_discount(self, price: float):  # Метод для применения скидки к цене.
        return price * (1 - self.discount_percent / 100)  # Возвращает цену после применения скидки (вычитая процент скидки).

    def __str__(self):  # Метод для строкового представления скидки.
        return f"Скидка (Описание={self.description}, Процент={self.discount_percent}%)"  # Возвращает строку с описанием и процентом скидки.

    
    """
    Класс Discount для представления скидки.

    Метод __init__:
        Инициализация скидки с описанием и процентом скидки.
        Пример: discount1 = Discount('Сезонная скидка', 15) создаст скидку с описанием 'Сезонная скидка' и процентом 15.

    Метод apply_discount:
        Статический метод, который принимает цену и процент скидки и возвращает цену после применения скидки.
        Пример: Discount.apply_discount(1000, 10) вернет 900.0.

    Метод __str__:
        Возвращает строковое представление скидки.
        Пример: print(discount1) выведет "Скидка Сезонная скидка, Процент=15%".
    """

