import pyexpat


class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed



from unittest import TestCase, main


class CarTest(TestCase):

    def setUp(self) -> None:
        self.car = Car('mazda', '3', 5, 40)

    def test_chek_atribute_make_non_corecly_given(self):
        self.assertEqual(self.car.make, 'mazda')
        with self.assertRaises(Exception) as ex:

            self.car.make = ''
        self.assertEqual('Make cannot be null or empty!', str(ex.exception))

    def test_chek_atribute_make_corecly_given(self):
        self.assertEqual(self.car.make, 'mazda')

    def test_chek_atribute_make_change_correct(self):
        self.car.make = 'opel'
        self.assertEqual('opel', self.car.make)

    def test_chek_atribute_model_non_corecly_given(self):
        self.assertEqual(self.car.model, '3')
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual('Model cannot be null or empty!', str(ex.exception))

    def test_chek_atribute_model_corecly_given(self):
        self.assertEqual(self.car.model, '3')

    def test_chek_fuel_consumption_not_given_correctly_negative_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -5
        self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))

    def test_chek_fuel_consumption_not_given_correctly__0__raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))

    def test_chek_fuel_consumption_given_correctly_raises(self):
        self.assertEqual(5, self.car.fuel_consumption)

    def test_chek_fuel_consumption_adding_correctly(self):
        self.car.fuel_consumption = 10
        self.assertEqual(10, self.car.fuel_consumption)

    def test_chek_fuel_capacity_given_correctly(self):
        self.assertEqual(40, self.car.fuel_capacity)

    def test_chek_fuel_capacity_adding_correctly(self):
        self.car.fuel_capacity = 10
        self.assertEqual(10, self.car.fuel_capacity)

    def test_chek_fuel_capacity_given__0__correctly(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_chek_fuel_capacity_given__negative__correctly(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -40
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_chek_fuel_amount_given_correctly(self):
        self.assertEqual(0, self.car.fuel_amount)

    def test_chek_fuel_amount_adding_correctly(self):
        self.car.fuel_amount = 10
        self.assertEqual(10, self.car.fuel_amount)

    def test_chek_fuel_amount_given__negative__correctly(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -40
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_given_negative_raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_given__0__raise(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_adding_more_fuel_than_fuel_capacity_of_the_car_correctly(self):
        self.car.refuel(9990)
        self.assertEqual(40, self.car.fuel_amount)

    def test_drive_with_enought_fuel(self):
        self.car.refuel(40)
        self.car.drive(5)
        self.assertEqual(39.75, self.car.fuel_amount)

    def test_drive_with_NOT_enought_fuel(self):
        self.car.refuel(1)
        with self.assertRaises(Exception) as ex:
            self.car.drive(50)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()
