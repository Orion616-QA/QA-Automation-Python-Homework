from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

engine = create_engine("postgresql://postgres:password@localhost:5432/postgres")
Base = declarative_base()

student_courses = Table(
    "student_courses",
    Base.metadata,
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True)
)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    courses = relationship("Course", secondary=student_courses, back_populates="students")

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String, nullable=False)
    students = relationship("Student", secondary=student_courses, back_populates="courses")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

""""Options for student and courses - create, update, delete"""
def add_new_student(first_name, last_name, course_ids=None):
    with Session() as session:
        courses = []
        if course_ids:
            courses = session.query(Course).filter(Course.id.in_(course_ids)).all()

        new_student = Student(first_name=first_name, last_name=last_name, courses=courses)
        session.add(new_student)
        session.commit()

def add_new_course(course_name):
    with Session() as session:
        new_course = Course(course_name=course_name)
        session.add(new_course)
        session.commit()

def update_student(student_id, first_name=None, last_name=None, course_ids=None):
    with Session() as session:
        student = session.query(Student).filter_by(id=student_id).first()
        if not student:
            raise ValueError("student not found")

        if first_name:
            student.first_name = first_name
        if last_name:
            student.last_name = last_name
        if course_ids is not None:
            courses = session.query(Course).filter(Course.id.in_(course_ids)).all()
            student.courses = courses

        session.commit()

def update_course(course_id, course_name=None):
    with Session() as session:
        course = session.query(Course).filter_by(id=course_id).first()
        if not course:
            raise ValueError("course not found")

        if course_name:
            course.course_name = course_name
            session.commit()

def delete_student(student_id):
    with Session() as session:
        student = session.query(Student).filter_by(id=student_id).first()
        if not student:
            raise ValueError("student not found")

        session.delete(student)
        session.commit()

def delete_course(course_id):
    with Session() as session:
        course = session.query(Course).filter_by(id=course_id).first()
        if not course:
            raise ValueError("course not found")

        session.delete(course)
        session.commit()

"""Get information options for student / course"""
def get_students_by_course_id(course_id):
    with Session() as session:
        course = session.query(Course).filter_by(id=course_id).first()
        if not course:
            raise ValueError("course not found")

        students_list = [f"{student.id}: {student.first_name} {student.last_name}" for student in course.students]
        return students_list

def get_courses_by_student_id(student_id):
    with Session() as session:
        student = session.query(Student).filter_by(id=student_id).first()
        if not student:
            raise ValueError("student not found")

        courses_list = [f"{course.id}: {course.course_name}" for course in student.courses]
        return courses_list