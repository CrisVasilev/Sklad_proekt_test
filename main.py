# Импортиране на класа Product
from models import Product

# Импортиране на colorama
from colorama import Fore, Style, init

# Инициализация на colorama
init(autoreset=True)

# Списък за продукти
products = []

# Име на файла
FILE_NAME = "products.txt"


# Функция за зареждане от файл
def load_products():

    try:

        # Отваряне на файла за четене
        with open(FILE_NAME, "r", encoding="utf-8") as file:

            # Четене на всеки ред
            for line in file:

                # Премахване на празните пространства
                line = line.strip()

                # Разделяне по запетая
                data = line.split(",")

                # Проверка дали има 3 стойности
                if len(data) == 3:

                    name = data[0]
                    quantity = int(data[1])
                    price = float(data[2])

                    # Създаване на продукт
                    product = Product(name, quantity, price)

                    # Добавяне в списъка
                    products.append(product)

    except FileNotFoundError:

        print(Fore.RED + "Файлът не съществува!")


# Функция за запис във файл
def save_products():

    # Отваряне на файла за запис
    with open(FILE_NAME, "w", encoding="utf-8") as file:

        # Обхождане на всички продукти
        for product in products:

            # Записване във файла
            file.write(product.to_file_format() + "\n")


# Функция за добавяне на продукт
def add_product():

    name = input("Въведи име на продукт: ")

    quantity = int(input("Въведи количество: "))

    price = float(input("Въведи цена: "))

    # Създаване на обект
    product = Product(name, quantity, price)

    # Добавяне в списъка
    products.append(product)

    # Запис във файл
    save_products()

    print(Fore.GREEN + "Продуктът е добавен успешно!")


# Функция за показване
def show_products():

    if len(products) == 0:

        print(Fore.RED + "Няма продукти!")

    else:

        print(Fore.CYAN + "\nСПИСЪК С ПРОДУКТИ:\n")

        # Обхождане
        for product in products:

            print("--------------------")

            product.show_info()


# Функция за търсене
def search_product():

    search_name = input("Въведи продукт за търсене: ")

    found = False

    for product in products:

        # Проверка
        if product.name.lower() == search_name.lower():

            print(Fore.YELLOW + "\nПродуктът е намерен:\n")

            product.show_info()

            found = True

    if not found:

        print(Fore.RED + "Продуктът не е намерен!")


# Зареждане на продуктите
load_products()

# Главно меню
while True:

    print(Fore.BLUE + "\n====== СКЛАД ======")

    print("1. Добави продукт")
    print("2. Покажи продукти")
    print("3. Търси продукт")
    print("4. Изход")

    choice = input("Избери опция: ")

    # Проверки
    if choice == "1":

        add_product()

    elif choice == "2":

        show_products()

    elif choice == "3":

        search_product()

    elif choice == "4":

        print(Fore.GREEN + "Изход от програмата.")

        break

    else:

        print(Fore.RED + "Невалиден избор!")