from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero('Ivan', 1, 100, 100)
        self.enemy = Hero('Mariq', 1, 100, 50)

    def test_corect_initislization(self):
        self.assertEqual('Ivan', self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_battle_cannot_fight_with_himself(self):
        some_hero = Hero('Ivan', 1, 100, 100)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(some_hero)
        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_battle_cannot_fight_with__0__hero_health(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_cannot_fight_with_NEGATIVE__hero_health(self):
        self.hero.health = -1
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_enemy_battles_with__0__helth(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

    def test_enemy_battles_with__NEGATIVE__health(self):
        self.enemy.health = -5
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

    def test_battle_outcome_hero_wins(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual('You win', result)

        self.assertEqual(2, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(105, self.hero.damage)

    def test_battle_outcome_EQUAL_ecspect_Draw(self):
        self.enemy.damage = 100
        result = self.hero.battle(self.enemy)
        self.assertEqual('Draw', result)

    def test_battle_outcome_hero_loses(self):
        self.hero.health = 10
        self.enemy.health = 300
        result = self.hero.battle(self.enemy)
        self.assertEqual('You lose', result)

        self.assertEqual(2, self.enemy.level)
        self.assertEqual(205, self.enemy.health)
        self.assertEqual(55, self.enemy.damage)

    def test_correct_str_representation(self):
        result = str(self.hero)
        self.assertEqual('Hero Ivan: 1 lvl\n'
                         'Health: 100\n'
                         'Damage: 100\n', result)


if __name__ == '__main__':
    main()
