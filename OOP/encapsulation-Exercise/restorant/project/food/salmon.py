from OOP.static_andclass_methods.hotel_rooms.project import MainDish


class Salmon(MainDish):
    GRAMS: int = 22

    def __init__(self, name: str, price: float):
        super().__init__(name, price, Salmon.GRAMS)