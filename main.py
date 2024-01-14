from sqlalchemy import func, desc, and_,select
from sqlalchemy.orm import joinedload, subqueryload

from src.models import Teacher, Student, Group, Discipline, Grade
from src.db import session


'''Знайти 5 студентів із найбільшим середнім балом з усіх предметів.'''
def query_1() -> list:
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
                        .select_from(Grade).join(Student)\
                        .group_by(Student.id)\
                        .order_by(desc('avg_grade'))\
                        .limit(5).all()
    
    return result

'''Знайти студента із найвищим середнім балом з певного предмета.'''
def query_2(discipline_id: int) -> list:
    result = session.query(Discipline.name, Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
                        .select_from(Grade).join(Student).join(Discipline)\
                        .filter(Discipline.id == discipline_id)\
                        .group_by(Student.id, Discipline.name)\
                        .order_by(desc('avg_grade'))\
                        .limit(1).all()
    
    return result 

'''Знайти середній бал у групах з певного предмета.'''
def query_3() -> list:
    result = session.query(Discipline.name, Group.name, func.round(func.avg(Grade.grade), 2).label('average_grade'))\
                        .select_from(Grade).join(Student).join(Discipline).join(Group)\
                        .filter()\
                        .group_by(Discipline.name, Group.name)\
                        .all()
    
    return result 

'''Знайти середній бал на потоці (по всій таблиці оцінок).'''
def query_4() -> list:
    result = session.query(func.round(func.avg(Grade.grade), 2).label('average_grade'))\
                        .select_from(Grade).all()
    
    return result 

'''Знайти які курси читає певний викладач.'''
def query_5(teacher_id:int) -> list:
    result = session.query(Teacher.fullname, Discipline.name)\
                        .select_from(Teacher).join(Discipline)\
                        .filter(Teacher.id==teacher_id)\
                        .all()
    
    return result 

'''Знайти список студентів у певній групі.'''
def query_6(group_id:int) -> list:
    result = session.query(Student.fullname, Group.name)\
                        .select_from(Student).join(Group)\
                        .filter(Group.id==group_id)\
                        .all()
    
    return result 

'''Знайти оцінки студентів у окремій групі з певного предмета.'''
def query_7(group_id,discipline_id:int) -> list:
    result = session.query(Discipline.name, Group.name, Student.fullname, Grade.grade)\
                        .select_from(Grade).join(Student).join(Discipline).join(Group)\
                        .filter(and_(Group.id==group_id), Discipline.id==discipline_id)\
                        .all()
    
    return result 

'''Знайти середній бал, який ставить певний викладач зі своїх предметів.'''
def query_8(teacher_id:int) -> list:
    result = session.query(Teacher.fullname, Discipline.name, func.round(func.avg(Grade.grade), 2).label('average_grade'))\
                        .select_from(Teacher).join(Discipline).join(Grade)\
                        .filter(Teacher.id==teacher_id)\
                        .group_by(Discipline.name, Teacher.fullname)\
                        .all()
    
    return result 

'''Знайти список курсів, які відвідує певний студент.'''
def query_9(student_id:int) -> list:
    result = session.query(Student.fullname, Discipline.name)\
                        .select_from(Grade).join(Student).join(Discipline)\
                        .filter(Student.id==student_id)\
                        .all()
    
    return result 

'''Список курсів, які певному студенту читає певний викладач'''
def query_10(student_id, teacher_id) -> list:
    result = session.query(Teacher.fullname, Student.fullname, Discipline.name)\
                        .select_from(Grade).join(Student).join(Discipline).join(Teacher)\
                        .filter(and_(Teacher.id==teacher_id, Student.id==student_id))\
                        .all()
    
    return result 


print('')
print('\033[31m','Q1: Знайти 5 студентів із найбільшим середнім балом з усіх предметів.','\033[0m')
for st in query_1():
    print(st)

print('')
print('\033[31m','Q2: Знайти студента із найвищим середнім балом з певного предмета','\033[0m')
print(query_2(5))

print('')
print('\033[31m','Q3: Знайти середній бал у групах з певного предмета.','\033[0m')
for d in query_3():
    print(d)

print('')
print('\033[31m','Q4: Знайти середній бал на потоці (по всій таблиці оцінок).','\033[0m')
print(query_4()[0][0])

print('')
print('\033[31m','Q5: Знайти які курси читає певний викладач.','\033[0m')
for d in query_5(2):
    print(d)

print('')
print('\033[31m','Q6: Знайти список студентів у певній групі.','\033[0m')
for st in query_6(3):
    print(st)

print('')
print('\033[31m','Q7: найти оцінки студентів у окремій групі з певного предмета.','\033[0m')
for r in query_7(2,6):
    print(r)

print('')
print('\033[31m','Q8: Знайти середній бал, який ставить певний викладач зі своїх предметів.','\033[0m')
for t in query_8(3):
    print(t)

print('')
print('\033[31m','Q9: Знайти список курсів, які відвідує певний студент.','\033[0m')
for st in query_9(34):
    print(st)

print('')
print('\033[31m','Q10: Список курсів, які певному студенту читає певний викладач','\033[0m')
for st in query_10(45, 3):
    print(st)

