from sqlalchemy import ForeignKey, create_engine, Column, Integer, String, Date, NVARCHAR, Identity, select
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship, sessionmaker

# Create the connection string for SQL Server
database_url = 'mssql+pyodbc://uzver:12345678@15-2-441-1-PREP/master?driver=ODBC+driver+17+for+SQL+Server'
engine = create_engine(database_url, echo=True)

Base = declarative_base()

class GROUPS(Base):
    __tablename__ = 'GROUPS'
    GROUP_ID: Mapped[int] = mapped_column(Identity(), primary_key=True)
    NAME_GROUP: Mapped[str] = mapped_column(NVARCHAR(25), nullable=False)
    COURSE: Mapped[int] = mapped_column(Integer)

class STUDENTS(Base):
    __tablename__ = 'STUDENTS'
    STUDENT_ID: Mapped[int] = mapped_column(primary_key=True)
    NAME_STUDENT: Mapped[str] = mapped_column(NVARCHAR(35), nullable=False)
    SURNAME_STUDENT: Mapped[str] = mapped_column(NVARCHAR(35), nullable=False)
    STUDENTS_SECONDNAME: Mapped[str] = mapped_column(NVARCHAR(35))
    BIRTHDAY: Mapped[Date] = mapped_column(Date)
    GROUP_ID: Mapped[int] = mapped_column(ForeignKey("GROUPS.GROUP_ID"))

    group: Mapped['GROUPS'] = relationship("GROUPS", back_populates="students")

class SUBJECTS(Base):
    __tablename__ = 'SUBJECTS'
    SUBJECT_ID: Mapped[int] = mapped_column(primary_key=True)
    SUBJECT_NAME: Mapped[str] = mapped_column(NVARCHAR(50), nullable=False)
    SUBJECT_HOURS: Mapped[int] = mapped_column(Integer)

class PLANN(Base):
    __tablename__ = 'PLANN'
    SUBJECT_ID: Mapped[int] = mapped_column(ForeignKey("SUBJECTS.SUBJECT_ID"), primary_key=True)
    GROUP_ID: Mapped[int] = mapped_column(ForeignKey("GROUPS.GROUP_ID"), primary_key=True)

class GROUPS(Base):
    __tablename__ = 'GROUPS'
    GROUP_ID: Mapped[int] = mapped_column(Identity(), primary_key=True)
    NAME_GROUP: Mapped[str] = mapped_column(NVARCHAR(25), nullable=False)
    COURSE: Mapped[int] = mapped_column(Integer)

    students: Mapped[list['STUDENTS']] = relationship("STUDENTS", back_populates="group")
    subjects: Mapped[list['SUBJECTS']] = relationship("SUBJECTS", secondary="PLANN")

# Create tables
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Insert Data
def insert_groups():
    group1 = GROUPS(NAME_GROUP='ПО135', COURSE=1)
    group2 = GROUPS(NAME_GROUP='ПО235', COURSE=2)
    group3 = GROUPS(NAME_GROUP='ПО335', COURSE=3)

    session.add(group1)
    session.add(group2)
    session.add(group3)
    session.commit()

def insert_subjects():
    subject1 = SUBJECTS(SUBJECT_NAME='Физика', SUBJECT_HOURS=200)
    subject2 = SUBJECTS(SUBJECT_NAME='Математика', SUBJECT_HOURS=120)
    subject3 = SUBJECTS(SUBJECT_NAME='Основы алгоритмизации', SUBJECT_HOURS=70)
    subject4 = SUBJECTS(SUBJECT_NAME='Проектирование БД', SUBJECT_HOURS=130)
    subject5 = SUBJECTS(SUBJECT_NAME='Средства визуального программирования', SUBJECT_HOURS=90)
    subject6 = SUBJECTS(SUBJECT_NAME='Объектно-ориентированное программирование', SUBJECT_HOURS=70)

    session.add(subject1)
    session.add(subject2)
    session.add(subject3)
    session.add(subject4)
    session.add(subject5)
    session.add(subject6)
    session.commit()

def insert_students():
    student1 = STUDENTS(NAME_STUDENT='Федоренко', SURNAME_STUDENT='П.', STUDENTS_SECONDNAME='Р.', BIRTHDAY='1997-12-25', GROUP_ID=1)
    student2 = STUDENTS(NAME_STUDENT='Зингел', SURNAME_STUDENT='О.', STUDENTS_SECONDNAME=None, BIRTHDAY='1985-12-25', GROUP_ID=1)
    student3 = STUDENTS(NAME_STUDENT='Савицкая', SURNAME_STUDENT='Н.', STUDENTS_SECONDNAME=None, BIRTHDAY='1987-09-22', GROUP_ID=2)
    student4 = STUDENTS(NAME_STUDENT='Ковальчук', SURNAME_STUDENT='М.', STUDENTS_SECONDNAME='E.', BIRTHDAY='1992-06-17', GROUP_ID=2)
    student5 = STUDENTS(NAME_STUDENT='Ковриго', SURNAME_STUDENT='Т.', STUDENTS_SECONDNAME='Р.', BIRTHDAY='1992-05-13', GROUP_ID=3)
    student6 = STUDENTS(NAME_STUDENT='Шарапо', SURNAME_STUDENT='Н.', STUDENTS_SECONDNAME=None, BIRTHDAY='1992-08-14', GROUP_ID=3)

    session.add(student1)
    session.add(student2)
    session.add(student3)
    session.add(student4)
    session.add(student5)
    session.add(student6)
    session.commit()

def insert_plann():
    plan1 = PLANN(GROUP_ID=1, SUBJECT_ID=1)
    plan2 = PLANN(GROUP_ID=1, SUBJECT_ID=2)
    plan3 = PLANN(GROUP_ID=2, SUBJECT_ID=3)
    plan4 = PLANN(GROUP_ID=2, SUBJECT_ID=4)
    plan5 = PLANN(GROUP_ID=3, SUBJECT_ID=5)
    plan6 = PLANN(GROUP_ID=3, SUBJECT_ID=6)

    session.add(plan1)
    session.add(plan2)
    session.add(plan3)
    session.add(plan4)
    session.add(plan5)
    session.add(plan6)
    session.commit()

# Example Select Query
def select_students():
    query = select(STUDENTS.NAME_STUDENT, STUDENTS.SURNAME_STUDENT, STUDENTS.STUDENTS_SECONDNAME, STUDENTS.BIRTHDAY, GROUPS.NAME_GROUP, GROUPS.COURSE)
    query = query.join(GROUPS, STUDENTS.GROUP_ID == GROUPS.GROUP_ID)
    result = session.execute(query).fetchall()
    
    for row in result:
        print(row)

# Running insert functions
# insert_groups()
# insert_subjects()
# insert_students()
# insert_plann()

# Running select query
select_students()

session.close()