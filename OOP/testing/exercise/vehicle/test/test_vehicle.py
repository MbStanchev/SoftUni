from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.car = Vehicle(35, 175)

    def test_instance_data(self):
        self.assertEqual(35, self.car.fuel)
        self.assertEqual(175, self.car.horse_power)
        self.assertEqual(35, self.car.capacity)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.car.fuel_consumption)

    def test_drive_expect_fuel_to_decrease(self):
        self.car.drive(20)
        self.assertEqual(10.0, self.car.fuel)

    def test_drive_expect_needed_fule_to_be_greaiter_then_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(9999)
        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_refuel_corectly(self):
        self.car.fuel -= 20
        self.car.refuel(10)
        self.assertEqual(25, self.car.fuel)

    def test_refuel_NON_corectly(self):
        self.car.fuel -= 20
        with self.assertRaises(Exception) as ex:
            self.car.refuel(40)
        self.assertEqual('Too much fuel', str(ex.exception))

    def test_str_return(self):
        self.assertEqual("The vehicle has 175 horse power with 35 fuel left and 1.25 fuel consumption", self.car.__str__())


if __name__ == "__main__":
    main()
