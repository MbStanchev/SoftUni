from OOP.inheritance_food_lab.project.employee import Employee
from OOP.inheritance_food_lab.project.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'

    