import logging
import pathlib
import requests
import subprocess
import time

from assertpy import assert_that
from logging import config



path_to_project = pathlib.Path(f"{pathlib.Path.home()}/Projects/AQA_course/")

logging.config.fileConfig(f"{path_to_project}/logging_config.ini")
logging.getLogger('sampleLogger')

def setup_teardown_steps(func):
    def wrapper(*args):
        logging.info("Precondition step:")
        logging.info("Run the HTTP server.")
        subprocess.Popen(("python3", "app.py"), cwd="Application")
        time.sleep(1)
        logging.info("The HTTP server was started!!")
        func(args)
        logging.info("Postcondition suite step:")
        logging.info("Application server stops.")
        subprocess.call(f"pkill -f app.py", shell=True)
        logging.info("The HTTP server was stopped!!")
    return wrapper

class TestSuiteRequestFunction:
    @setup_teardown_steps
    def test_post_request_function(self):
        logging.info("Verify \"POST\" request.")
        url = 'http://127.0.0.1:8080/upload'
        path_to_file = {"image": open('mars_photo1.jpg', 'rb')}
        response = requests.post(url, files=path_to_file)

        logging.info("Verify the response status is 201.")
        (assert_that(response.status_code, f'Request \"POST\" was unsuccessful with status {response.status_code}')
         .is_equal_to(201))

        logging.info("Verify the response context is \"image_url\" "
                     "with url \"http://127.0.0.1:8080/uploads/mars_photo1.jpg\".")
        expected_result = {'image_url': 'http://127.0.0.1:8080/uploads/mars_photo1.jpg'}
        (assert_that(response.json(), f'Error. Status-code: {response.status_code}, {response.text}')
         .is_equal_to(expected_result))

    @setup_teardown_steps
    def test_get_request_function(self):
        logging.info("Verify \"GET\" request.")
        url = 'http://127.0.0.1:8080/image/mars_photo1.jpg'
        header = {"Content-Type": "text"}
        response = requests.get(url, headers=header)

        logging.info("Verify the response status is 200.")
        (assert_that(response.status_code, f'Request \"GET\" was unsuccessful with status {response.status_code}')
         .is_equal_to(200))

        logging.info("Verify the response context is \"image_url\" "
                     "with url \"http://127.0.0.1:8080/uploads/mars_photo1.jpg\".")
        expected_result = {'image_url': 'http://127.0.0.1:8080/uploads/mars_photo1.jpg'}
        (assert_that(response.json(), f'Error. Status-code: {response.status_code}, {response.text}')
         .is_equal_to(expected_result))

    @setup_teardown_steps
    def test_delete_request_function(self):
        logging.info("Verify \"DELETE\" request.")
        url = 'http://127.0.0.1:8080/delete/mars_photo1.jpg'
        response = requests.delete(url)

        logging.info("Verify the response status is 200.")
        (assert_that(response.status_code, f'Request \"GET\" was unsuccessful with status {response.status_code}')
         .is_equal_to(200))

        logging.info("Verify the response context is \"image_url\" "
                     "with url \"http://127.0.0.1:8080/uploads/mars_photo1.jpg\".")
        expected_result = {'message': 'Image mars_photo1.jpg deleted'}
        (assert_that(response.json(), f'Error. Status-code: {response.status_code}, {response.text}')
         .is_equal_to(expected_result))
