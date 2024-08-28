class Product: # Определение класса Product, представляющего отдельный продукт.

    def __init__(self, name: str, price: float):         # Инициализация товара с атрибутами name (название) и price (цена)
        self.name = name        
        self.price = price      

    def __str__(self):         # Метод для строкового представления экземпляра класса Product.
        return f"Продукт (Название={self.name}, Цена={self.price})"        # Возвращает строку, содержащую название и цену продукта.
    
    """
    Класс Product

    Этот класс представляет товар в интернет-магазине.

    Метод __init__:
        Конструктор инициализирует объект Product с двумя атрибутами: name (название товара) и price (цена товара).
        Пример: product1 = Product("Laptop", 1000) создаст товар с названием "Laptop" и ценой 1000.

    Метод __str__:
        Возвращает строковое представление объекта, чтобы его можно было удобно вывести с помощью print.
        Пример: print(product1) выведет Product(name=Laptop, price=1000).
    """