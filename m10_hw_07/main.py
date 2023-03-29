from sqlalchemy import func, desc, select, and_

from database.models import Teacher, Student, Discipline, Grade, Group
from database.db import session


def select_one():
    """
    Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    SELECT s.fullname, ROUND(AVG(g.grade), 2) as avg_grade
    FROM grades g
    LEFT JOIN students s ON s.id = g.student_id
    GROUP BY s.id
    ORDER BY avg_grade DESC
    LIMIT 5;
    :return:
    """
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
             .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    # order_by(Grade.grade.desc())
    return result


def select_two():
    """
    SELECT d.name, s.fullname, ROUND(AVG(g.grade), 2) as avg_grade
    FROM grades g
    LEFT JOIN students s ON s.id = g.student_id
    LEFT JOIN disciplines d ON d.id = g.discipline_id
    WHERE d.id = 5
    GROUP BY s.id
    ORDER BY avg_grade DESC
    LIMIT 1;
    :return:
    """
    result = session.query(
                        Discipline.name,
                        Student.fullname,
                        func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
                    .select_from(Grade).join(Student).join(Discipline)\
                    .filter(Discipline.id == 5)\
                    .group_by(Student.id, Discipline.name).order_by(desc('avg_grade')).limit(1).first()
    return result


def select_12():
    """
    -- Оцінки студентів у певній групі з певного предмета на останньому занятті.
    select s.id, s.fullname, g.grade, g.date_of
    from grades g
    join students s on s.id = g.student_id
    where g.discipline_id = 3 and s.group_id = 3 and g.date_of = (
        select max(date_of)
        from grades g2
        join students s2 on s2.id = g2.student_id
        where g2.discipline_id = 3 and s2.group_id = 3
    );
    :return:
    """
    subquery = (select(func.max(Grade.date_of)).join(Student).filter(and_(
                    Grade.discipline_id == 3, Student.group_id == 3
                )).scalar_subquery())

    result = session.query(Student.id, Student.fullname, Grade.grade, Grade.date_of)\
                    .select_from(Grade)\
                    .join(Student)\
                    .filter(and_(
                        Grade.discipline_id == 3, Student.group_id == 3, Grade.date_of == subquery
                    )).all()
    return result


if __name__ == '__main__':
    # print(select_one())
    # print(select_two())
    print(select_12())
