class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTest(TestCase):

    def test_is_inishalized_corectly_without_data(self):
        integ_obj = IntegerList()
        self.assertEqual([], integ_obj._IntegerList__data)

    def test_is_inishalized_corectly_with_wrong_data(self):
        integ_obj = IntegerList("foo", 5.5)
        self.assertEqual([], integ_obj._IntegerList__data)

    def test_is_inishalized_corectly_with_corect_data(self):
        integ_obj = IntegerList(5, 10, "ff")
        self.assertEqual([5, 10], integ_obj._IntegerList__data)

    def test_get_data(self):
        integ_obj = IntegerList(5, 10, "ff")
        self.assertEqual([5, 10], integ_obj._IntegerList__data)

        result = integ_obj.get_data()
        self.assertEqual([5, 10], result)

    def test_adding_non_integer_raises(self):
        cat = IntegerList(5)
        self.assertEqual([5], cat.get_data())
        with self.assertRaises(ValueError) as ex:
            cat.add('5')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_adding_integer(self):
        cat = IntegerList(6, 77)
        self.assertEqual([6, 77], cat.get_data())

        cat.add(55)
        self.assertEqual([6, 77, 55], cat.get_data())

    def test_remove_index_raises_exception(self):
        pass

    def test_remove_index(self):
        cat = IntegerList(6, 77)
        cat.remove_index(0)
        self.assertEqual([77], cat.get_data())

    def test_rest_get_invalid_index(self):
        cat = IntegerList(6, 77)

        with self.assertRaises(IndexError) as ex:
            cat.get(2)
        self.assertEqual("Index is out of range", str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            cat.get(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_valid_index_returns_el(self):
        cat = IntegerList(5, 22)
        result = cat.get(1)
        self.assertEqual(22, result)

    def test_insert_index_out_of_range_raises(self):
        cat = IntegerList(5, 22)

        with self.assertRaises(IndexError) as ex:
            cat.insert(5, 3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_index_not_integer_raises(self):
        cat = IntegerList(5, 3)

        with self.assertRaises(ValueError) as ex:
            cat.insert(1, '5')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_on_valid_index(self):
        cat = IntegerList(5, 3)
        cat.insert(1, 10000)
        self.assertEqual([5, 10000, 3], cat.get_data())

    def test_get_biggest(self):
        cat = IntegerList(5, 10000, -555555, 3, 0)
        result = cat.get_biggest()
        self.assertEqual(10000, result)

    def test_get_index(self):
        cat = IntegerList(5, 10000, -555555, 3, 0)
        result = cat.get_index(3)
        self.assertEqual(3, result)


if __name__ == "__main__":
    main()
