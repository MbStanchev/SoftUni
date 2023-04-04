from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):

    def test_name_input(self):
        self.cat = Mammal('Totka', 'houcehoud', 'mrrr')
        self.assertEqual(self.cat.name, 'Totka')
        self.assertEqual(self.cat.type, 'houcehoud')
        self.assertEqual(self.cat.sound, 'mrrr')
        self.assertEqual(self.cat._Mammal__kingdom, 'animals')

    def test_make_sound(self):
        cat = Mammal('Totka', 'houcehoud', 'mrrr')
        self.assertEqual(cat.make_sound(), 'Totka makes mrrr')

    def test_get_kingdom(self):
        self.cat = Mammal('Totka', 'houcehoud', 'mrrr')
        self.assertEqual('animals', self.cat.get_kingdom())

    def test_info(self):
        self.cat = Mammal('Totka', 'houcehoud', 'mrrr')
        self.assertEqual('Totka is of type houcehoud', self.cat.info())


if __name__ == '__main__':
    main()
