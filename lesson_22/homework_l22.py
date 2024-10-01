import logging
import pathlib
import subprocess
import traceback

from logging import config
from pony.orm import Set, db_session, PrimaryKey, select, core

from lesson_22.BASE.pony_orm_db_client import PonyOrmDbClient
from lesson_22.BASE.psql_client import PSQLClient

path_to_project = pathlib.Path(f"{pathlib.Path.home()}/Projects/AQA_course/")

logging.config.fileConfig(f"{path_to_project}/logging_config.ini")
logging.getLogger('sampleLogger')

subprocess.run("sudo systemctl start postgresql", shell=True)

# The "postgresql" client to delete created tables finally
# Please use your own data for DB "course_list"
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
    # The client to connect by PonyORM to course_list DB
    # Please use your own data for DB "course_list"
    client_course_list = PonyOrmDbClient(provider='postgres',
                                         user='mtrykoz',
                                         password='12345678',
                                         host='localhost',
                                         database='course_list')

    class Student(client_course_list.db.Entity):
        students_name = PrimaryKey(str, auto=False)
        courses = Set('Course')

    class Course(client_course_list.db.Entity):
        course_name = PrimaryKey(str, auto=False)
        students = Set('Student')

    client_course_list.db.generate_mapping(create_tables=True)

    def get_selected_courses(courses_list) -> list:
        selected_courses = list(select(course for course in Course if course.course_name in courses_list))
        return selected_courses

    def set_student_with_courses():
        action_2 = True
        while action_2:
            new_student_name = input("Enter STUDENT name (for finish enter \"q\"): ")
            if new_student_name == "q":
                action_2 = False
            else:
                print("The exist course list:")
                for course in Course.select():
                    print(f"  - {course.course_name}")
                new_course_list = input("Enter a COURSE for new student from the exist course list, "
                                        "separating with a comma: ").split(", ")
                try:
                    Student(students_name=new_student_name, courses=get_selected_courses(new_course_list))
                except core.CacheIndexError:
                    logging.error(f"Cannot create STUDENT: instance with \"{new_student_name}\" already exists!!!")
                    print("Try to enter other student name or choice the function to add new course to student!!!")
            print("!==================!")

    def add_new_course():
        action_1 = True
        while action_1:
            new_course_name = input("Enter COURSE name (for finish enter \"q\"): ")
            if new_course_name == "q":
                action_1 = False
            else:
                try:
                    Course(course_name=new_course_name)
                except core.CacheIndexError:
                    logging.error(f"Cannot create Course: instance with \"{new_course_name}\" already exists.")
                    print("Try to enter other course name!!!")
        print("!==================!")

    def get_student_data():
        selected_student = input("Enter STUDENT name for the searching: ")
        select_courses_for_student = select(student.courses
                                            for student in Student if student.students_name == selected_student)
        print("!===== Result =====!")
        print(f"The \"{selected_student}\" student selected the following course(s):")
        for course in list(select_courses_for_student):
            print(f"  - \"{course.course_name}\"")
        print("!==================!")

    def get_course_data():
        selected_course = input("Enter COURSE name for the searching: ")
        select_course_with_students = select(course.students
                                            for course in Course if course.course_name == selected_course)
        print("!===== Result =====!")
        print(f"The following students are (is) taking the course \"{selected_course}\":")
        for student in list(select_course_with_students):
            print(f"  - {student.students_name}")
        print("!==================!")

    def delete_student_from_course():
        deleted_student = input("Enter STUDENT name for the deleting: ")
        deleted_course = input("Enter COURSE for the deleting: ")
        select_student = list(select(student for student in Student if student.students_name == deleted_student))[0]
        course_for_delete = list(select(course for course in Course if course.course_name == deleted_course))[0]
        select_student.courses.remove(course_for_delete)

    # Create default test courses list to DB
    with db_session:
        courses = [Course(course_name=f"Course_{number}") for number in range(1, 6)]

    while True:
        print("Make your action choice:")
        print("    enter \"1\" - add new COURSE to DB")
        print("    enter \"2\" - add new STUDENT to course")
        print("    enter \"3\" - delete STUDENT from COURSE")
        print("    enter \"4\" - select STUDENT with courses from DB")
        print("    enter \"5\" - select COURSE with students from DB")
        print("    enter \"q\" - Quit from the application")
        choice_action = input("Enter here: ")

        with db_session:
            if choice_action == "1":
                add_new_course()
            elif choice_action == "2":
                set_student_with_courses()
            elif choice_action == "3":
                delete_student_from_course()
            elif choice_action == "4":
                get_student_data()
            elif choice_action == "5":
                get_course_data()
            elif choice_action == "q":
                break
            else:
                pass

except Exception as exception:
    print(traceback.format_exc())

finally:
    client.execute_data_db("DROP TABLE course_student;")
    client.execute_data_db("DROP TABLE course;")
    client.execute_data_db("DROP TABLE student;")
    logging.info("Delete table \"course_student\", \"course\", \"student\".")

    subprocess.run("sudo systemctl stop postgresql", shell=True)
