import logging
import pathlib
import requests
import subprocess
import time

from logging import config

path_to_project = pathlib.Path(f"{pathlib.Path.home()}/Projects/AQA_course/")

logging.config.fileConfig(f"{path_to_project}/logging_config.ini")
logging.getLogger('sampleLogger')

logging.info("Precondition step:")
logging.info("Run the HTTP server.")
server = subprocess.Popen(("python3", "app.py"), cwd="Application")
time.sleep(1)
logging.info("The HTTP server was started!!")

logging.info("Verify \"POST\" request.")
url = 'http://127.0.0.1:8080/upload'
path_to_file = {"image": open('mars_photo1.jpg', 'rb')}
response = requests.post(url, files=path_to_file)
if response.status_code == 201:
    created_data = response.json()
    logging.info(f'The data was created: {created_data}')
else:
    logging.error(f'Error. Status-code: {response.status_code}, {response.text}')

logging.info("Verify \"GET\" request.")
url = 'http://127.0.0.1:8080/image/mars_photo1.jpg'
header = {"Content-Type": "text"}
response = requests.get(url, headers=header)
if response.status_code == 200:
    created_data = response.json()
    logging.info(f'The data was created: {created_data}')
else:
    logging.error(f'Error. Status-code: {response.status_code}, {response.text}')

logging.info("Verify \"DELETE\" request.")
url = 'http://127.0.0.1:8080/delete/mars_photo1.jpg'
response = requests.delete(url)
if response.status_code == 200:
    created_data = response.json()
    logging.info(f'The data was created: {created_data}')
else:
    logging.error(f'Error. Status-code: {response.status_code}, {response.text}')

logging.info("Postcondition suite step:")
logging.info("Application server stops.")
subprocess.call(f"pkill -f app.py", shell=True)
logging.info("The HTTP server was stopped!!")


