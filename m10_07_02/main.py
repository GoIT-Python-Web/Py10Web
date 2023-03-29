from datetime import datetime

from sqlalchemy.orm import joinedload, subqueryload
from sqlalchemy import and_

from database.db import session
from database.models import Teacher, Student, ContactPerson, TeacherStudent


def get_students():
    students = session.query(Student).join(Student.teachers).all()
    for s in students:
        print(vars(s))
        print(f"{[t.fullname for t in s.teachers]}")


def get_students_load():
    students = session.query(Student).options(joinedload(Student.teachers)).all()
    for s in students:
        print(vars(s))
        print(f"{[t.fullname for t in s.teachers]}")


def get_students_sub():
    students = session.query(Student).options(subqueryload(Student.teachers)).all()
    for s in students:
        print(vars(s))
        print(f"{[t.fullname for t in s.teachers]}")


def get_teachers():
    teachers = session.query(Teacher).options(joinedload(Teacher.students)) \
        .filter(and_(
            Teacher.start_work >= datetime(year=2020, month=1, day=1),
            Teacher.start_work <= datetime(year=2022, month=12, day=31)
        )).all()

    for t in teachers:
        print(vars(t))
        print(f"{[s.fullname for s in t.students]}")


def get_students_contact():
    students = session.query(Student).join(Student.contacts).all()
    for s in students:
        print(vars(s))
        print(f"{[c.fullname for c in s.contacts]}")


def custom_get_students():
    students = session.query(Student.id, Student.fullname, Teacher.fullname, ContactPerson.fullname)\
                .select_from(Student).join(TeacherStudent).join(Teacher).join(ContactPerson).all()
    print(students)


if __name__ == '__main__':
    # get_students()
    # get_students_sub()
    # get_teachers()
    # get_students_contact()
    custom_get_students()
