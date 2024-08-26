class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course = []
        self.grade = {}

    def middle_rating(self):
        total_grade = 0
        count = 0
        for grade_list in self.grade.values():
            total_grade += sum(grade_list)
            count += len(grade_list)
            if count == 0:
                return 0
        return total_grade / count

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nCредняя оценка за лекции: {self.middle_rating()}"

    def __lt__(self, other):
        return self.middle_rating() < other.middle_rating()

    def __gt__(self, other):
        return self.middle_rating() > other.middle_rating()

    def __eq__(self, other):
        return self.middle_rating() == other.middle_rating()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course = []

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.course and course in student.course_in_progress:
            if course in student.grade:
                student.grade[course] += [grade]
            else:
                student.grade[course] = [grade]
        else:
            print('Ошибкаффффф')


class Student:
    def __init__(self, name, surname, gender):
        self.course_in_progress = []
        self.gender = gender
        self.surname = surname
        self.name = name
        self.finished_courses = []
        self.grade = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.course_in_progress and course in lecturer.course:
            if course in lecturer.grade:
                lecturer.grade[course] += [grade]
            else:
                lecturer.grade[course] = [grade]
        else:
            print('Ошибка.')

    def middle_rating(self):
        total_grade = 0
        count = 0
        for grade_list in self.grade.values():
            total_grade += sum(grade_list)
            count += len(grade_list)
            if count == 0:
                return 0
        return total_grade / count

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Cредняя оценка за домашние задания: {self.middle_rating()}\n'
                f'Курсы в процессе обучения:{self.course_in_progress}\nЗавершенные курсы:{self.finished_courses}')

    def __lt__(self, other):
        return self.middle_rating() < other.middle_rating()

    def __gt__(self, other):
        return self.middle_rating() > other.middle_rating()

    def __eq__(self, other):
        return self.middle_rating() == other.middle_rating()


def calculate_average_homework_grade(students, course):
    total_grades = 0
    count = 0

    for student in students:
        if course in student.courses_in_progress:
            if course in student.grade:
                total_grades += sum(student.grade[course])
                count += len(student.grade[course])

    if count == 0:
        return 0
    return total_grades / count


def calculate_average_lecture_grade(lecturers, course):
    total_grades = 0
    count = 0

    for lecturer in lecturers:
        if course in lecturer.course:
            if course in lecturer.grade:
                total_grades += sum(lecturer.grade[course])
                count += len(lecturer.grade[course])

    if count == 0:
        return 0
    return total_grades / count


some_student = Student('Студент', 'Студентович', 'MALE')
some_student.course_in_progress += ['Python']
some_student.finished_courses += ['Git']
some_student_1 = Student('Студент_1', 'Студентович_1', 'MALE')
some_student_1.course_in_progress += ['JAVA']
some_student_1.finished_courses += ['HTML']
some_lecture = Lecturer('Лектор', 'Лекторович')
some_lecture.course += ['Python']
some_lecture_1 = Lecturer('Лектор_1', 'Лекторович_1')
some_lecture_1.course += ['JAVA']
some_mentor = Mentor('Ментор', 'Менторович')
some_mentor_1 = Mentor('Ментор_1', 'Менторович_1')
some_student.rate_lecturer(some_lecture, 'Python', 10)
some_student_1.rate_lecturer(some_lecture_1, 'JAVA', 2)
some_student_1.rate_lecturer(some_lecture_1, 'JAVA', 4)
some_student.rate_lecturer(some_lecture, 'Python', 2)
some_reviewer = Reviewer("Ревьюер", 'Ревьюерович')
some_reviewer.course += ['Python']
some_reviewer_1 = Reviewer("Ревьюер_1", 'Ревьюерович_1')
some_reviewer_1.course += ['JAVA']
some_reviewer.rate_student(some_student, 'Python', 5)
some_reviewer.rate_student(some_student, 'Python', 10)
some_reviewer.rate_student(some_student, 'Python', 9)
some_reviewer.rate_student(some_student, 'Python', 10)
some_reviewer_1.rate_student(some_student_1, 'JAVA', 2)
some_reviewer_1.rate_student(some_student_1, 'JAVA', 2)
some_reviewer_1.rate_student(some_student_1, 'JAVA', 1)
some_reviewer_1.rate_student(some_student_1, 'JAVA', 2)
print(some_reviewer)
print('-------------------------------------------')
print(some_reviewer_1)
print('-------------------------------------------')
print(some_student)
print('-------------------------------------------')
print(some_student_1)
print('-------------------------------------------')
print(some_lecture)
print('-------------------------------------------')
print(some_lecture_1)
print('-------------------------------------------')
print(f'Средняя оценка среди лекторов: {calculate_average_lecture_grade([some_lecture, some_lecture_1], 'Python')}')
print('-------------------------------------------')
print(f'Средняя оценка среди студентов: {calculate_average_lecture_grade([some_lecture, some_lecture_1], 'JAVA')}')
print('-------------------------------------------')
print(some_lecture > some_lecture_1)
print('-------------------------------------------')
print(some_student == some_student_1)
