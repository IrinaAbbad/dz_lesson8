from classes.order import Order
from classes.product import Product
from classes.discount import Discount
from classes.customer import Customer
import random

# Создание продуктов (пять товаров).
products = [
    Product("товар1", 300),
    Product("товар2", 700), 
    Product("товар3", 50), 
    Product("товар4", 200), 
    Product("товар5", 150)
]

# Создание клиентов (три клиента).
customers = [
    Customer("Иван"),  
    Customer("Ольга"),  
    Customer("Анна")  
]

# Создание скидок (две скидки).
discounts = [
    Discount("Сезонная скидка", 10),  
    Discount("Скидка по промокоду", 15)  ]

# Создание заказов с применением случайных скидок.
orders = [
    Order([products[0], products[2]], random.choice(discounts)),  # Создаем заказ с товарами и случайной скидкой.
    Order([products[1]], random.choice(discounts)),  # Создаем заказ без скидки.
    Order([products[3], products[4]], random.choice(discounts)),  # Создаем заказ с товарами и случайной скидкой.
    Order([products[2], products[4]], random.choice(discounts)),  # Создаем заказ без скидки.
    Order([products[0], products[1], products[3]], random.choice(discounts))  # Создаем заказ с товарами и случайной скидкой.
]

# Добавление заказов клиентам случайным образом.
for order in orders:  # Для каждого заказа из списка заказов...
    random.choice(customers).add_order(order)  # ...выбираем случайного клиента и добавляем ему заказ.

# Вывод информации о клиентах и их заказах.
for customer in customers:  # Для каждого клиента из списка клиентов...
    print(customer)  # ...выводим информацию о клиенте.
    for order in customer.orders:  # Для каждого заказа клиента...
        print(order)  # ...выводим информацию о заказе.

# Вывод общей суммы всех заказов и общего количества заказов.
print(f"Общее количество заказов: {Order.total_orders()}")  # Выводим общее количество всех заказов.
print(f"Общая сумма всех заказов: {Order.total_sum()}")  # Выводим общую сумму всех заказов.
