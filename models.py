# Клас Product
# Използва се за създаване на продукти

class Product:

    # Конструктор
    def __init__(self, name, quantity, price):

        # Име на продукта
        self.name = name

        # Количество
        self.quantity = quantity

        # Цена
        self.price = price

    # Метод за показване на информация
    def show_info(self):

        print(f"Продукт: {self.name}")
        print(f"Количество: {self.quantity}")
        print(f"Цена: {self.price:.2f} лв")

    # Метод за конвертиране към текст
    # Използва се при запис във файл
    def to_file_format(self):

        return f"{self.name},{self.quantity},{self.price}"

    # Метод за добавяне на количество
    def add_quantity(self, amount):

        self.quantity += amount

    # Метод за премахване на количество
    def remove_quantity(self, amount):

        if amount > self.quantity:

            print("Няма достатъчна наличност!")

        else:

            self.quantity -= amount