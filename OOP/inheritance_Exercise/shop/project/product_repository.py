from OOP.inheritance_Exercise.shop.project.drink import Drink
from OOP.inheritance_Exercise.shop.project.food import Food
from OOP.inheritance_Exercise.shop.project.product import Product
from typing import List


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        product = [p for p in self.products if p.name == product_name]
        if product:
            return product[0]

    def remove(self, product_name):
        product = self.find(product_name)

        if product:
            self.products.remove(product)

    def __repr__(self):
        return "\n".join([f'{p}: {p.quantity}' for p in self.products])


food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)
