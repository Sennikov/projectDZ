class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def __str__(self):
        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_rating}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):

        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    # def rate_hw(self, student, course, grade):
    #    if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
    #        if course in student.grades:
    #            student.grades[course] += [grade]
    #        else:
    #            student.grades[course] = [grade]
    #    else:
    #        return 'Ошибка'


class Lecturer(Mentor):

    def __init__(self, name, surname):


        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def __str__(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):

        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):

        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


# Лекторы курсов
best_lecturer_1 = Lecturer('Алексей', 'Иванов')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Егор', 'Егорович')
best_lecturer_2.courses_attached += ['PHP']

best_lecturer_3 = Lecturer('Сергей', 'Лебедев')
best_lecturer_3.courses_attached += ['Python']

# Проверяющие за курсом
cool_reviewer_1 = Reviewer('Николай', 'Николаев')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['PHP']

cool_reviewer_2 = Reviewer('Some', 'Buddy')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['PHP']

# Студенты - курсы которые изучают и завершенные курсы
student_1 = Student('Дмитрий', 'Дмитриенко', 'Мужской')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Роман', 'Матусовский', 'Мужской')
student_2.courses_in_progress += ['PHP']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Александр', 'Сосновкий', 'Мужской')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']

# Оценки лекторов за лекции
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)

student_1.rate_hw(best_lecturer_2, 'Python', 5)
student_1.rate_hw(best_lecturer_2, 'Python', 7)
student_1.rate_hw(best_lecturer_2, 'Python', 8)

student_1.rate_hw(best_lecturer_1, 'Python', 7)
student_1.rate_hw(best_lecturer_1, 'Python', 8)
student_1.rate_hw(best_lecturer_1, 'Python', 9)

student_2.rate_hw(best_lecturer_2, 'PHP', 10)
student_2.rate_hw(best_lecturer_2, 'PHP', 8)
student_2.rate_hw(best_lecturer_2, 'PHP', 9)

student_3.rate_hw(best_lecturer_3, 'Python', 5)
student_3.rate_hw(best_lecturer_3, 'Python', 6)
student_3.rate_hw(best_lecturer_3, 'Python', 7)

# Выставляем студентам оценки за ДЗ
cool_reviewer_1.rate_hw(student_1, 'Python', 5)
cool_reviewer_1.rate_hw(student_1, 'Python', 7)
cool_reviewer_1.rate_hw(student_1, 'Python', 4)

cool_reviewer_2.rate_hw(student_2, 'PHP', 4)
cool_reviewer_2.rate_hw(student_2, 'PHP', 6)
cool_reviewer_2.rate_hw(student_2, 'PHP', 8)

cool_reviewer_2.rate_hw(student_3, 'Python', 3)
cool_reviewer_2.rate_hw(student_3, 'Python', 6)
cool_reviewer_2.rate_hw(student_3, 'Python', 8)
cool_reviewer_2.rate_hw(student_3, 'Python', 5)
cool_reviewer_2.rate_hw(student_3, 'Python', 10)
cool_reviewer_2.rate_hw(student_3, 'Python', 4)

# Вывод проверяющих
print(f'Перечень проверяющих:\n\n{cool_reviewer_1}\n\n{cool_reviewer_2}')
print()
print()

# Вывод студентов
print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()
print()

# Выводим лекторов
print(f'Перечень лекторов:\n\n{best_lecturer_1}\n\n{best_lecturer_2}\n\n{best_lecturer_3}')
print()
print()

# Результат сравнения студентов по средним оценкам за ДЗ
print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')
print()

# Результат сравнения лекторов по средним оценкам за лекции
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname} = {best_lecturer_1 > best_lecturer_2}')
print()

# Список студентов
student_list = [student_1, student_2, student_3]

# Список лекторов
lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]


# Функцию для подсчета средней оценки за ДЗ

def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for stud in student_list:
        if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


# Функция для подсчета средней оценки за лекции всех лекторов


def lecturer_rating(lecturer_list, course_name):

    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


# Результат подсчета средней оценки по всем студентам
print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()

# Результат подсчета средней оценки по всем лекорам
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()