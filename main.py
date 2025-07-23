# src/model.py

class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: {self.description}, Price: {self.price}, Quantity: {self.quantity}"

class Smartphone(Product):
    def __init__(self, name, description, price, quantity, quality, model, storage, color):
        super().__init__(name, description, price, quantity)
        self.quality = quality
        self.model = model
        self.storage = storage
        self.color = color

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, origin, growth_time, color):
        super().__init__(name, description, price, quantity)
        self.origin = origin
        self.growth_time = growth_time
        self.color = color

class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []
        Category.category_count += 1

    def add_product(self, product):
        self.products.append(product)
        Category.product_count += 1

    def average_price(self):
        if not self.products:  # Проверяем, есть ли товары в категории
            return 0.0  # Возвращаем 0, если товаров нет
        total_price = sum(product.price for product in self.products)
        return total_price / len(self.products)  # Возвращаем среднюю цену

    def __str__(self):
        return f"Category: {self.name}, Description: {self.description}, Average Price: {self.average_price()}"

# Пример использования
if __name__ == "__main__":
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, "High", "S23 Ultra", "256GB", "Gray")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, "High", "15", "512GB", "Gray")
    lawn_grass1 = LawnGrass("Green Lawn", "High-quality grass", 500.0, 100, "USA", "7 days", "Green")

    print(smartphone1)
    print(smartphone2)
    print(lawn_grass1)

    category1 = Category("Смартфоны", "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")
    category1.add_product(smartphone1)
    category1.add_product(smartphone2)

    category2 = Category("Трава газонная", "Качественная трава для вашего газона")
    # Не добавляем товары в category2, чтобы проверить случай с отсутствием товаров

    print(category1)
    print(category1.products)
    print("Category Count:", Category.category_count)
    print("Product Count:", Category.product_count)

    print(category2)
    print(category2.products)
    print("Category Count:", Category.category_count)
    print("Product Count:", Category.product_count)

    # Пример использования итерации по категории
    for product in category1:
        print(product)

    # Проверка средней цены в категории без товаров
    print("Average price in category2:", category2.average_price())  # Ожидается 0.0

