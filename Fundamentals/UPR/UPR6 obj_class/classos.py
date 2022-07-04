class Class:
    __students_count = 22

    def __init__(self, name_class):
        self.name_class = name_class
        self.students = []
        self.grades = []

    def add_student(self, name, grade:float):
        if Class.__students_count > 0:
            self.students.append(name)
            self.grades.append(grade)
            Class.__students_count -= 1

    def get_average_grade(self):
        result = sum(self.grades)/len(self.grades)
        return result

    def __repr__(self):
        return f"The students in {self.name_class}: {', '.join(self.students)}. Average grade: {self.get_average_grade():.2f}."

a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
