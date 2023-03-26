class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):

    def test_worker_is_initialize_correctly(self):
        person = Worker("Mitko", 2000, 20)
        self.assertEqual("Mitko", person.name)
        self.assertEqual(2000, person.salary)
        self.assertEqual(20, person.energy)

    def test_if_the_energy_is_incremented_after_rest(self):
        person = Worker("Mitko", 2000, 20)
        self.assertEqual(20, person.energy)

        person.rest()
        self.assertEqual(21, person.energy)

    def test_error_raise_when_try_to_work_with_zero_energy(self):
        person = Worker("Mitko", 2000, 0)
        with self.assertRaises(Exception) as ex:
            person.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_error_raise_when_try_to_work_with_negative_energy(self):
        person = Worker("Mitko", 2000, -2)
        with self.assertRaises(Exception) as ex:
            person.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_monay_raised_after_work(self):
        person = Worker("Mitko", 2000, 20)
        self.assertEqual(0, person.money)
        person.work()
        self.assertEqual(2000, person.money)
        person.work()
        self.assertEqual(4000, person.money)

    def test_energy_decreasing_after_working(self):
        person = Worker("Mitko", 2000, 20)
        self.assertEqual(20, person.energy)
        person.work()
        self.assertEqual(19, person.energy)

    def test_if_get_info_returne_proper_str(self):
        person = Worker("Mitko", 2000, 20)
        self.assertEqual("Mitko has saved 0 money.", person.get_info())
        person.work()
        self.assertEqual("Mitko has saved 2000 money.", person.get_info())


if __name__ == '__main__':
    main()
