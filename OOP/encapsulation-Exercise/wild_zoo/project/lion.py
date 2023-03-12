from OOP.static_andclass_methods.hotel_rooms.project import Animal


class Lion(Animal):
    MONEY = 50

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, Lion.MONEY)

