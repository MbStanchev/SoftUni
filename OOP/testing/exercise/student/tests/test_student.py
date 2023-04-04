from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):

    def setUp(self) -> None:
        self.some_drunk = Student('Rakiq', {'math': ['yes', 'no']})
        self.other_drunk = Student('Rakiq', {})

    def test_inisalizing_data_with_courses(self):
        self.assertEqual('Rakiq', self.some_drunk.name)
        self.assertEqual({'math': ['yes', 'no']}, self.some_drunk.courses)

    def test_inisalizing_data_WITOUHT_courses(self):
        self.assertEqual('Rakiq', self.some_drunk.name)
        self.assertEqual({}, self.other_drunk.courses)

    def test_enroll_course_in_courses_NOT_in_ouer_corces_with_corse_note(self):
        result = self.some_drunk.enroll("Python", ['test', 'solid'], 'Y')
        self.assertEqual(2, len(self.some_drunk.courses))
        self.assertEqual(2, len(self.some_drunk.courses["Python"]))
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_course_in_courses_NOT_in_ouer_corces_WITHOUT_corse_note(self):
        result = self.some_drunk.enroll("Python", ['test', 'solid'], 'N')
        self.assertEqual(2, len(self.some_drunk.courses))
        self.assertEqual(0, len(self.some_drunk.courses["Python"]))
        self.assertEqual("Course has been added.", result)

    def test_enroll_course_in_courses_in_ouer_corces_WITHOUT_corse_note(self):
        self.some_drunk.enroll("Python", ['test', 'solid'], 'n')
        result = self.some_drunk.enroll("Python", ['*args', '**kwargs'])
        self.assertEqual(2, len(self.some_drunk.courses))
        self.assertEqual(2, len(self.some_drunk.courses['Python']))

    def test_not_course_in_courses(self):
        with self.assertRaises(Exception) as ex:
            self.some_drunk.add_notes('Beer and fries', 'good, very good')
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_in_course_in_courses(self):
        result = self.some_drunk.add_notes("math", "math is the shit")
        self.assertEqual("Notes have been updated", result)

    def test_leave_course_sucsesfily(self):
        result = self.some_drunk.leave_course("math")
        self.assertEqual("Course has been removed", result)

    def test_leave_course_UNsucsesfily(self):
        with self.assertRaises(Exception) as ex:
            self.other_drunk.leave_course("Biology")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
