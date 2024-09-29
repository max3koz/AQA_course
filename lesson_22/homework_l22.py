import logging
import pathlib
import subprocess
import time
import traceback

from logging import config
from random import randint, random, sample

from pony.orm import Required, Set, db_session, PrimaryKey, select

# from lesson_22.BASE.db_objects import client_pony, Course, Student
from lesson_22.BASE.pony_orm_db_client import PonyOrmDbClient
from lesson_22.BASE.psql_client import PSQLClient

path_to_project = pathlib.Path(f"{pathlib.Path.home()}/Projects/AQA_course/")

logging.config.fileConfig(f"{path_to_project}/logging_config.ini")
logging.getLogger('sampleLogger')

subprocess.run("sudo systemctl start postgresql", shell=True)
time.sleep(1)

# The "postgresql" client to delete created table finally
dbname = "course_list"
user = "mtrykoz"
password = "12345678"
host = "127.0.0.1"
port = 5432

client = PSQLClient(dbname=dbname,
                    user=user,
                    password=password,
                    host=host,
                    port=port)

try:
    client_pony = PonyOrmDbClient(provider='postgres',
                         user='mtrykoz',
                         password='12345678',
                         host='localhost',
                         database='course_list')

    class Student(client_pony.db.Entity):
        id = PrimaryKey(int, auto=True)
        students_name = Required(str)
        courses = Set('Course')

    class Course(client_pony.db.Entity):
        id = PrimaryKey(int, auto=True)
        course_name = Required(str)
        students = Set('Student')

    client_pony.db.generate_mapping(create_tables=True)


    def generate_course_to_student(courses_list) -> list:
        qty_course = randint(1, len(courses) - 1)
        return sample(courses_list, qty_course)

    with db_session:
        courses = [Course(course_name = f"Course_1{number}") for number in range(5)]
        students = [Student(students_name = f"Student_{number}", courses=generate_course_to_student(courses))
                    for number in range(1, 20)]

        Course.select().show()
        print()
        Student.select().show()

        print(students[1].students_name, students[1].courses)

        selected_student = input("Enter student name: ")

        select_courses_for_student = select(student.courses for student in Student
                                            if student.students_name == selected_student)

        print(f"{selected_student} courses list are/is:")
        for course in list(select_courses_for_student):
            print(course.course_name)



except Exception as exception:
    print(traceback.format_exc())

finally:
    # input("lsdfhbgklsjdhflk ")
    logging.info("Delete table \"course_student\", \"course\", \"student\".")
    client.execute_data_db("DROP TABLE course_student;")
    client.execute_data_db("DROP TABLE course;")
    client.execute_data_db("DROP TABLE student;")

    subprocess.run("sudo systemctl stop postgresql", shell=True)
