class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False



from unittest import TestCase, main


class CatTest(TestCase):

    def test_cat_name(self):
        kote = Cat("Totka")
        self.assertEqual("Totka", kote.name)

    def test_cat_size_increase_after_eat(self):
        kote = Cat('Totka')
        self.assertEqual(0, kote.size)
        kote.eat()
        self.assertEqual(1, kote.size)

    def test_cat_is_fed_after_eating(self):
        kote = Cat('Totka')
        self.assertFalse(kote.fed)
        kote.eat()
        self.assertTrue(kote.fed)

    def test_cat_cannot_eat_after_is_fed_raise(self):
        kote = Cat('Totka')
        kote.eat()
        with self.assertRaises(Exception) as ex:
            kote.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_cannot_fall_asleap_if_not_fed(self):
        kote = Cat('Totka')
        self.assertFalse(kote.fed)

        with self.assertRaises(Exception) as ex:
            kote.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_cannot_sleep_after_sleeping(self):
        kote = Cat('Totka')
        self.assertFalse(kote.fed)
        self.assertFalse(kote.sleepy)
        kote.eat()
        kote.sleep()
        self.assertTrue(kote.sleep)
        kote.sleep()
        self.assertFalse(kote.sleepy)


if __name__ == '__main__':
    main()
