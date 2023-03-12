from OOP.static_andclass_methods.hotel_rooms.project import Animal


class Tiger(Animal):
    MONEY = 45

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, Tiger.MONEY)


