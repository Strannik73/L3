from sqlalchemy import create_engine, Column, Integer, String, Date, Float, NVARCHAR, Identity, ForeignKey, select, or_, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, Mapped, mapped_column
from datetime import date


# Создание подключения
database_url = 'mssql+pyodbc://uzver:12345678@15-2-441-1-PREP/master?driver=ODBC+driver+17+for+SQL+Server'
engine = create_engine(database_url, echo=True)

Base = declarative_base()

# Определение модели STUD
class stud(Base):
    __tablename__ = 'stud'

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    last_name: Mapped[str] = mapped_column(NVARCHAR(25), nullable=False)
    f_name: Mapped[str] = mapped_column(NVARCHAR(25), nullable=False)
    s_name: Mapped[str] = mapped_column(NVARCHAR(25), nullable=True)
    form: Mapped[str] = mapped_column(NVARCHAR(10), nullable=False, default='очная')
    faculty: Mapped[str] = mapped_column(NVARCHAR(10), nullable=False, default='ФПМ')
    year: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    all_h: Mapped[int] = mapped_column(Integer, nullable=True)
    inclass_h: Mapped[int] = mapped_column(Integer, nullable=True)
    br_date: Mapped[Date] = mapped_column(Date)
    in_date: Mapped[Date] = mapped_column(Date)
    exm: Mapped[Float] = mapped_column(Float, nullable=True)

class teach(Base):
    __tablename__ = 'teach'

    id: Mapped[int] = mapped_column(Identity(), primary_key=True)
    last_name: Mapped[str] = mapped_column(NVARCHAR(25), nullable=False)
    f_name: Mapped[str] = mapped_column(NVARCHAR(25), nullable=False)
    s_name: Mapped[str] = mapped_column(NVARCHAR(25), nullable=True)
    subj: Mapped[str] = mapped_column(NVARCHAR(150), nullable=False)
    form: Mapped[str] = mapped_column(NVARCHAR(10), nullable=False, default='очная')
    faculty: Mapped[str] = mapped_column(NVARCHAR(10), nullable=False, default='ФПМ')
    year: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    hours: Mapped[int] = mapped_column(Integer, nullable=True)
    br_date: Mapped[Date] = mapped_column(Date)
    start_work_date: Mapped[Date] = mapped_column(Date)

# Создание таблиц
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Вставка данных в таблицу STUD
def insert_students():
    students_data = [
        ('Стрынгель', 'К', 'null', 'заочная', 'ФПК', 1, 300, 100, '1983-12-12', '2016-09-01', 8),
        ('Козлова', 'Д', 'Е', 'заочная', 'ФПК', 2, 300, 100, '1983-10-12', '2015-09-01', 8.4),
        ('Федоров', 'Н', 'Н', 'заочная', 'ФПК', 3, 300, 100, '1981-12-07', '2014-09-01', 7),
        ('Рингель', 'П', 'О', 'заочная', 'ФПК', 3, 300, 100, '1973-02-15', '2016-09-01', 8),
        ('Бежик', 'Н', 'Н', 'вечерняя', 'ФПК', 1, 500, 400, '1993-12-11', '2016-09-01', 4.5),
        ('Осипчик', 'Н', 'Н', 'вечерняя', 'ФПК', 1, 500, 400, '1983-12-16', '2015-09-01', 7.7),
        ('Белый', 'С', 'С', 'вечерняя', 'ФПК', 2, 450, 370, '1987-06-27', '2015-09-01', 6.7),
        ('Ботяновский', 'А', 'С', 'вечерняя', 'ФПК', 2, 450, 370, '1987-07-23', '2015-09-01', 7.6),
        ('Слободницкий', 'С', 'А', 'вечерняя', 'ФПК', 2, 450, 370, '1987-08-03', '2015-09-01', 6.7),
        ('Рогатка', 'П', 'Р', 'очная', 'ФПМ', 1, 500, 450, '1986-10-27', '2016-09-01', 7.4),
        ('Федоренко', 'П', 'Р', 'очная', 'ФПМ', 1, 500, 450, '1995-04-26', '2016-09-01', 5.6),
        ('Зингель', 'П', 'В', 'очная', 'ФПМ', 2, 500, 450, '1990-04-25', '2015-09-01', 3.4),
        ('Михеенок', 'Л', 'Н', 'очная', 'ФПМ', 2, 500, 450, '1989-03-13', '2015-09-01', 5.3),
        ('Савицкая', 'Л', 'Н', 'очная', 'ФПМ', 3, 450, 400, '1995-07-05', '2014-09-01', 7.7),
        ('Ковальчук', 'О', 'Е', 'заочная', 'ФПМ', 1, 350, 100, '1964-05-23', '2016-09-01', 7.6),
        ('Заболотная', 'Л', 'И', 'заочная', 'ФПМ', 1, 350, 100, '1986-09-14', '2016-09-01', 4.7),
        ('Ковриго', 'И', 'null', 'заочная', 'ФПМ', 2, 360, 120, '1992-03-01', '2015-09-01', 7.7),
        ('Шарапо', 'М', 'null', 'заочная', 'ФПМ', 2, 360, 120, '1997-03-25', '2015-09-01', 8.7),
        ('Сафроненко', 'Н', 'Л', 'заочная', 'ФПМ', 3, 370, 130, '1992-05-25', '2014-09-01', 7.7),
        ('Зайцева', 'Т', 'Я', 'заочная', 'ФПМ', 3, 370, 130, '1994-07-25', '2014-09-01', 5.6),
    ]

    for student in students_data:
        student_obj = stud(
            last_name=student[0],
            f_name=student[1],
            s_name=student[2],
            form=student[3],
            faculty=student[4],
            year=student[5],
            all_h=student[6],
            inclass_h=student[7],
            br_date=student[8],
            in_date=student[9],
            exm=student[10]
        )
        session.add(student_obj)

    session.commit()

# Вставка данных в таблицу TEACH
def insert_teachers():
    teachers_data = [
        ('Скворцов', 'К', 'null', 'Дифференциальные исчисления', 'очная', 'ФПМ', 1, 150, '1983-12-12', '2016-09-01'),
        ('Скворцов', 'К', 'null', 'Геометрия и алгебра', 'очная', 'ФПМ', 1, 200, '1983-12-12', '2016-09-01'),
        ('Сидоренко', 'Л', 'К', 'Теория вероятности', 'очная', 'ФПМ', 1, 100, '1983-12-12', '2016-09-01'),
        ('Скворцов', 'К', 'null', 'Дифференциальные исчисления', 'заочная', 'ФПМ', 1, 34, '1983-12-12', '2016-09-01'),
        ('Сидоренко', 'Л', 'К', 'Геометрия и алгебра', 'заочная', 'ФПМ', 1, 50, '1983-12-12', '2016-09-01'),
        ('Сидоренко', 'Л', 'К', 'Теория вероятности', 'заочная', 'ФПМ', 1, 16, '1983-12-12', '2016-09-01'),
        ('Круглов', 'К', 'Д', 'Теория множеств', 'очная', 'ФПМ', 2, 150, '1986-08-25', '2014-09-01'),
        ('Круглов', 'К', 'Д', 'Методы численного анализа', 'очная', 'ФПМ', 2, 150, '1986-08-25', '2014-09-01'),
        ('Загорова', 'К', 'Д', 'Прикладная статистика', 'очная', 'ФПМ', 2, 150, '1979-10-05', '2010-09-01'),
        ('Круглов', 'К', 'Д', 'Теория множеств', 'заочная', 'ФПМ', 2, 40, '1986-08-25', '2014-09-01'),
        ('Круглов', 'К', 'Д', 'Методы численного анализа', 'заочная', 'ФПМ', 2, 40, '1986-08-25', '2014-09-01'),
        ('Загорова', 'К', 'Д', 'Прикладная статистика', 'заочная', 'ФПМ', 2, 40, '1979-10-05', '2010-09-01'),
        ('Зуров', 'П', 'null', 'Философия', 'очная', 'ФПМ', 3, 50, '1978-07-12', '2016-09-01'),
        ('Зуров', 'П', 'null', 'Социология', 'очная', 'ФПМ', 3, 50, '1978-07-12', '2016-09-01'),
        ('Сидоренко', 'Л', 'К', 'Методы машинного обучения', 'очная', 'ФПМ', 3, 150, '1983-12-12', '2016-09-01'),
        ('Журков', 'К', 'null', 'Методы выпуклой оптимизации', 'очная', 'ФПМ', 3, 150, '1986-11-16', '2015-09-01'),
        ('Курт', 'П', 'Р', 'Философия', 'заочная', 'ФПМ', 3, 20, '1978-07-12', '2016-09-01'),
        ('Курт', 'П', 'Р', 'Социология', 'заочная', 'ФПМ', 3, 20, '1978-07-12', '2016-09-01'),
        ('Сидоренко', 'Л', 'К', 'Методы машинного обучения', 'заочная', 'ФПМ', 3, 50, '1983-12-12', '2016-09-01'),
        ('Журков', 'К', 'null', 'Методы выпуклой оптимизации', 'заочная', 'ФПМ', 3, 40, '1986-11-16', '2015-09-01'),
        ('Скворцов', 'К', 'null', 'Основы алгоритмизации', 'заочная', 'ФПК', 1, 30, '1978-02-12', '2016-09-01'),
        ('Скворцов', 'К', 'null', 'Основы операционных систем', 'заочная', 'ФПК', 1, 20, '1978-02-12', '2016-09-01'),
        ('Сидоренко', 'Л', 'К', 'Объектно-ориенторованное программирование', 'заочная', 'ФПК', 1, 50, '1983-12-12', '2016-09-01'),
        ('Скворцов', 'К', 'null', 'Основы алгоритмизации', 'вечерняя', 'ФПК', 1, 100, '1978-02-12', '2016-09-01'),
        ('Скворцов', 'К', 'null', 'Основы операционных систем', 'вечерняя', 'ФПК', 1, 100, '1978-02-12', '2016-09-01'),
        ('Сидоренко', 'Л', 'К', 'Объектно-ориенторованное программирование', 'вечерняя', 'ФПК', 1, 200, '1983-12-12', '2016-09-01'),
        ('Кипеня', 'Д', 'А', 'Компонентное программирование', 'заочная', 'ФПК', 2, 30, '1984-01-09', '2013-09-01'),
        ('Зорков', 'К', 'А', 'Средства визуального программирования', 'заочная', 'ФПК', 2, 40, '1989-12-12', '2016-09-01'),
        ('Иридова', 'Т', 'К', 'Объектно-ориенторованное программирование', 'заочная', 'ФПК', 1, 50, '1983-04-12', '2016-09-01'),
        ('Кипеня', 'Д', 'А', 'Компонентное программирование', 'вечерняя', 'ФПК', 2, 130, '1984-01-09', '2013-09-01'),
        ('Зорков', 'К', 'А', 'Средства визуального программирования', 'вечерняя', 'ФПК', 2, 140, '1989-12-12', '2016-09-01'),
        ('Иридова', 'Т', 'К', 'Объектно-ориенторованное программирование', 'вечерняя', 'ФПК', 2, 110, '1983-04-12', '2016-09-01'),
        ('Курт', 'П', 'Р', 'Философия', 'заочная', 'ФПК', 3, 20, '1978-07-12', '2016-09-01'),
        ('Курт', 'П', 'Р', 'Социология', 'заочная', 'ФПК', 3, 20, '1978-07-12', '2016-09-01'),
        ('Иридова', 'Т', 'К', 'Современные языки программирования', 'заочная', 'ФПК', 3, 30, '1983-04-12', '2016-09-01'),
        ('Иридова', 'Т', 'К', 'Тестирование программного обеспечения', 'заочная', 'ФПК', 3, 30, '1983-04-12', '2016-09-01'),
        ('Курт', 'П', 'Р', 'Философия', 'вечерняя', 'ФПК', 3, 40, '1978-07-12', '2016-09-01'),
        ('Курт', 'П', 'Р', 'Социология', 'вечерняя', 'ФПК', 3, 40, '1978-07-12', '2016-09-01'),
        ('Иридова', 'Т', 'К', 'Современные языки программирования', 'вечерняя', 'ФПК', 3, 150, '1983-04-12', '2016-09-01'),
        ('Иридова', 'Т', 'К', 'Тестирование программного обеспечения', 'вечерняя', 'ФПК', 3, 160, '1983-04-12', '2016-09-01'),
    ]

    for teacher in teachers_data:
        teacher_obj = teach(
            last_name=teacher[0],
            f_name=teacher[1],
            s_name=teacher[2],
            subj=teacher[3],
            form=teacher[4],
            faculty=teacher[5],
            year=teacher[6],
            hours=teacher[7],
            br_date=teacher[8],
            start_work_date=teacher[9]
        )
        session.add(teacher_obj)

    session.commit()

# Вставка данных
insert_students()
insert_teachers()

# def nom1():
#     query = select(stud.last_name()).filter(or_(stud.last_name.like('%б%'),
#                                                 stud.last_name.like('%о%')))
#     result = session.execute(query).fetchall()
#     for row in result:
#         print(row[0])
# nom1()

# def nom2():
#     query = select(stud).filter(or_(stud.last_name.like('к%'),
#                                                 stud.s_name == 'null'))
#     result = session.execute(query).fetchall()
#     for row in result:
#         print(row.last_name, row.f_name, row.s_name, row.form, row.faculty, row.year, row.all_h, row.inclass_h, row.br_date, row.in_date, row.exm)
# nom2()

# def nom3():
#     query = select(stud).filter(or_(stud.last_name >= 8))
#     result = session.execute(query).fetchall()
#     for row in result:
#         print(row.last_name, row.f_name, row.s_name, row.form, row.faculty, row.year, row.all_h, row.inclass_h, row.br_date, row.in_date, row.exm)
# nom3()

# def nom4():
#     query = select(stud).filter(or_(func.length(stud.last_name) != 7, 
#                                                  stud.last_name.like('%a%')))
#     result = session.execute(query).fetchall()
#     for row in result:
#         print(row.last_name, row.f_name, row.s_name, row.form, row.faculty, row.year, row.all_h, row.inclass_h, row.br_date, row.in_date, row.exm)
# nom4()

# =========================================================
# def nom5():
#     query = select(stud).filter(stud.faculty == 'ФПМ',
#                                 stud.form == 'очная', 
#                                 stud.year <= 2).order_by(stud.s_name)
#     result = session.execute(query).fetchall()
#     for row in result:
#         print(row.last_name, row.f_name, row.s_name)
# nom5()

# def nom6():
#     query = select(stud).filter(stud.faculty == 'ФПК',
#                                 stud.form == 'заочная', 
#                                 stud.exm > 6).order_by(stud.exm.desc()) 
#     result = session.execute(query).fetchall()
#     for row in result:
#         print(row.last_name, row.f_name, row.s_name, row.exm)
# nom6()

def nom7():
    query = select(teach).filter(teach.faculty == 'ФПК',
                                teach.form == 'заочная', 
                                teach.exm > 6).order_by(teach.exm.desc()) 
    result = session.execute(query).fetchall()
    for row in result:
        print(row.last_name, row.f_name, row.s_name, row.subj, row.form, row.faculty, row.year, row.hours, row.br_date, row.start_work_date,)
nom7()

        teacher_obj = teach(
            last_name=teacher[0],
            f_name=teacher[1],
            s_name=teacher[2],
            subj=teacher[3],
            form=teacher[4],
            faculty=teacher[5],
            year=teacher[6],
            hours=teacher[7],
            br_date=teacher[8],
            start_work_date=teacher[9]
        )
session.close()
