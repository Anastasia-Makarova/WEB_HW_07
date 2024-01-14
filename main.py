from sqlalchemy import func, desc, and_,select

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
def query_7(group_id,discipline_id) -> list:
    result = session.query(Discipline.name, Group.name, Student.fullname, Grade.grade)\
                        .select_from(Grade).join(Student).join(Discipline).join(Group)\
                        .filter(and_(Group.id==group_id), Discipline.id==discipline_id)\
                        .all()
    
    return result 

''' SELECT d.name, sg.group_name, s.fullname,  g.grade 
    FROM grades g
    JOIN students s ON g.student_id = s.student_id 
    JOIN disciplines d ON g.discipline_id = d.discipline_id 
    JOIN students_groups sg
WHERE sg.group_id = 3 AND d.discipline_id = 5'''

'''Знайти середній бал, який ставить певний викладач зі своїх предметів.'''
def query_8() -> list:
    result = session.query(Discipline.name, Student.fullname, func.round(func.avg(), 2).label(''))\
                        .select_from().join().join()\
                        .filter()\
                        .group_by()\
                        .order_by(desc())\
                        .limit().all()
    
    return result 

'''Знайти список курсів, які відвідує певний студент.'''
def query_9() -> list:
    result = session.query(Discipline.name, Student.fullname, func.round(func.avg(), 2).label(''))\
                        .select_from().join().join()\
                        .filter()\
                        .group_by()\
                        .order_by(desc())\
                        .limit().all()
    
    return result 

'''Список курсів, які певному студенту читає певний викладач'''
def query_10() -> list:
    result = session.query(Discipline.name, Student.fullname, func.round(func.avg(), 2).label(''))\
                        .select_from().join().join()\
                        .filter()\
                        .group_by()\
                        .order_by(desc())\
                        .limit().all()
    
    return result 






'''Extra -2 Оцінки студентів у певній групі з певного предмета на останньому занятті.'''

def query_12(group_id: int, discipline_id:int):
    subquery = (select(Grade.date_of)\
                .join(Student).join(Group)\
                .where(and_\
                       (Grade.discipline_id == discipline_id,\
                       Group.id == group_id))\
                .order_by(desc(Grade.date_of))\
                .scalar_subquery())
    
    result = session.query(Discipline.name, Student.fullname, Group.name, Grade.date_of, Grade.grade)\
                .select_from(Grade).join(Student).join(Discipline).join(Group)\
                    .filter(and_(\
                        Discipline.id == discipline_id,\
                        Group.id == group_id,\
                        Grade.date_of == subquery))\
                        .order_by(desc(Grade.date_of))\
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
for st in query_6(2):
    print(st)


print('')
print('\033[31m','Q7: найти оцінки студентів у окремій групі з певного предмета.','\033[0m')
for r in query_7(2,5):
    print(r)



# print('')
# print('\033[31m','Q8: Знайти середній бал, який ставить певний викладач зі своїх предметів.','\033[0m')
# print(query_8())


# print('')
# print('\033[31m','Q9: Знайти список курсів, які відвідує певний студент.','\033[0m')
# print(query_9())


# print('')
# print('\033[31m','Q10: Список курсів, які певному студенту читає певний викладач','\033[0m')
# print(query_10())

# print('')
# print('\033[31m','Q12: Extra -2 Оцінки студентів у певній групі з певного предмета на останньому занятті','\033[0m')
# print(query_12(1, 2))