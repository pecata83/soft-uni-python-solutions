class Class:

    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        self.students.append(name)
        self.grades.append(grade)

    def get_students_names(self):
        return ', '.join(self.students)

    def get_average_grade(self):
        total_grade = 0
        for grade in self.grades:
            total_grade += grade
        return total_grade / len(self.students)

    def __repr__(self):
        return f"The students in {self.name}: {self.get_students_names()}. Average grade: {self.get_average_grade():.3}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
