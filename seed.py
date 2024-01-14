from datetime import date, datetime, timedelta
from random import randint, choice
import faker
from sqlalchemy import select

from src.models import Teacher, Student, Discipline, Grade, Group
from src.db import session

fake = faker.Faker()


NUMBER_OF_TEACHERS = 5
NUMBER_OF_STUDENTS = 50


def date_range(start: date, end: date) -> list:
    result = []
    current_date = start
    while current_date <= end:
        if current_date.isoweekday() < 6:
            result.append(current_date)
        current_date += timedelta(1)
    return result

def fill_data():
    disciplines = [
        'Math', 
        'Physics', 
        'History', 
        'Literature', 
        'Coding', 
        'English'
        'Biology'
        ]

    students_groups = [
        'Py022', 
        'C023', 
        'JS021'
        ]
    
    def seed_teachers():
        for _ in range(NUMBER_OF_TEACHERS):
            teacher = Teacher(fullname=fake.name())
            session.add(teacher)
        session.commit()

    def seed_disciplines():
        teacher_ids = session.scalars(select(Teacher.id)).all()
        for discipline in disciplines:
            session.add(Discipline(name=discipline, teacher_id=choice(teacher_ids)))
        session.commit()

    def seed_groups():
        for group in students_groups:
            session.add(Group(name=group))
        session.commit()

    def seed_students():
        group_ids = session.scalars(select(Group.id)).all()
        for _ in range(NUMBER_OF_STUDENTS):
            student = Student(fullname=fake.name(), group_id=choice(group_ids))
            session.add(student)
        session.commit()


    def seed_grades():

        start_date = datetime.strptime('2023-09-01', '%Y-%m-%d')
        end_date = datetime.strptime('2023-12-30', '%Y-%m-%d')

        d_range = date_range(start=start_date, end=end_date)
        discipline_ids = session.scalars(select(Discipline.id)).all()
        student_ids = session.scalars(select(Student.id)).all()

        for d in d_range:
            random_id_discipline = choice(discipline_ids)
            random_id_student = [choice(student_ids) for _ in range(NUMBER_OF_STUDENTS)]


            for student_id in random_id_student:
                grade = Grade(
                    grade =randint(1, 5),
                    date_of=d,
                    student_id=student_id,
                    discipline_id=random_id_discipline
                )

            session.add(grade)
        session.commit()

    seed_teachers()
    seed_disciplines()
    seed_groups()
    seed_students()
    seed_grades()



if __name__ == '__main__':
    fill_data()

