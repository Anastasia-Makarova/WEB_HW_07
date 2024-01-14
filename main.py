from sqlalchemy import func, desc

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
def query_2(discipline_id: int):
    result = session.query(Discipline.name, Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
                        .select_from(Grade).join(Student).join(Discipline)\
                        .filter(Discipline.id == discipline_id)\
                        .group_by(Student.id, Discipline.name)\
                        .order_by(desc('avg_grade'))\
                        .limit(1).all()
    
    return result
    



'''Знайти середній бал у групах з певного предмета.'''


'''Знайти середній бал на потоці (по всій таблиці оцінок).'''


'''Знайти які курси читає певний викладач.'''


'''Знайти список студентів у певній групі.'''


'''Знайти оцінки студентів у окремій групі з певного предмета.'''


'''Знайти середній бал, який ставить певний викладач зі своїх предметів.'''


'''Знайти список курсів, які відвідує певний студент.'''


'''Список курсів, які певному студенту читає певний викладач'''



print('')
print('\033[31m','Q1: Знайти 5 студентів із найбільшим середнім балом з усіх предметів.','\033[0m')
for st in query_1():
    print(st)

print('')
print('\033[31m','Q2: Знайти студента із найвищим середнім балом з певного предмета','\033[0m')
print(query_2(5))

'''Знайти середній бал у групах з певного предмета.'''


'''Знайти середній бал на потоці (по всій таблиці оцінок).'''


'''Знайти які курси читає певний викладач.'''


'''Знайти список студентів у певній групі.'''


'''Знайти оцінки студентів у окремій групі з певного предмета.'''


'''Знайти середній бал, який ставить певний викладач зі своїх предметів.'''


'''Знайти список курсів, які відвідує певний студент.'''


'''Список курсів, які певному студенту читає певний викладач'''