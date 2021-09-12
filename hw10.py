class Table:
    def __init__(self):
        self.students = []

    def __str__(self):
        ret = "Students: \n"
        for student in self.students:
            ret += f"\t{student} \n"
        return ret
    def add_student(self, student):
        self.students.append(student)

    def sort_students_by_age(self):
        self.students = sorted(self.students, key=lambda s: s.age)

    def sort_students_by_grade(self):
        self.students = sorted(self.students, key=lambda s: s.grade)
    def add_homework_for_all_students(self, homework):
        for i in range(len(self.students)):
            students[i].add_homework(Homework(homework.name, homework.description, homework.complexity, homework.status))

    def change_homework_status_for_student(self, student_index, homework_index, status):
        students[student_index].homeworks[homework_index].change_status(status)

class Homework:
    def __init__(self, name, description, complexity, status):
        self.name = name
        self.description = description
        self.complexity = complexity
        self.status = status
        self.grade = 0

    def __str__(self):
        return f"{self.name}, {self.description}, {self.complexity}, {self.status}"
    def change_status(self, status):
        self.status = status



class Student:
    def __init__(self, name, age, subscribed_course):
        self.name = name
        self.age = age
        self.grade = 0
        self.subscribed_course = subscribed_course
        self.homeworks = []

    def __str__(self):
        ret = f"{self.name}, age: {self.age}, grade: {self.grade}, course: {self.subscribed_course}:\n"
        ret = ret + "\tHomeworks:\n"
        for h in self.homeworks:
            ret = ret + "\t\t" + str(h) + "\n"
        return ret

    def add_homework(self, homework):
        self.homeworks.append(homework)
    def change_homework_status(self, homework_index, status):
        self.homeworks[homework_index].change_status(status)


students = [
    Student("Student 1", 12, "Python"), Student("Student 2", 16, "Python"), Student(
        "Student 3", 15, "Python"), Student("Student 4", 14, "Python")
]

table = Table()

for student in students:
    table.add_student(student)

table.add_homework_for_all_students(Homework("Homework1", "Description1", 2, False))
table.add_homework_for_all_students(Homework("Homework2", "Description2", 2, False))

table.change_homework_status_for_student(2, 0, True)

table.sort_students_by_age()
print("Sorted student by age")
print(table)

input()