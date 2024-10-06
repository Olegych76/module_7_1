import os


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        if not os.path.exists(self.__file_name):  # Если файл не существует, создаем его
            file = open(self.__file_name, 'w')
            file.close()

    def get_products(self):  # Запрашиваем список товаров из файла
        file = open(self.__file_name, 'r')
        str_ = file.read()
        file.close()
        return str_

    def add(self, *products):  # Добавляем товары в список товаров
        str_ = self.get_products()
        file = open(self.__file_name, 'a')
        for product in products:
            if str(product) in str_:
                print(f'Товар {product} уже есть в магазине')
            else:
                file.write(f'{product}\n')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
