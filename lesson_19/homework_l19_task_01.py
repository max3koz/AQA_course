import logging
import pathlib
import requests

from logging import config

path_to_project = pathlib.Path(f"{pathlib.Path.home()}/Projects/AQA_course/")

logging.config.fileConfig(f"{path_to_project}/logging_config.ini")
logging.getLogger('sampleLogger')

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}
expected_response_status_code = 200

response = requests.get(url, params=params)

if response.status_code == expected_response_status_code:
    data: list[dict] = response.json()["photos"]
    for index in range(len(data)):
        response = requests.get(data[index]['img_src'])
        if response.status_code == expected_response_status_code:
            with open(f'mars_photo{index + 1}.jpg', 'wb') as file:
                file.write(response.content)
            logging.info(f"The photo mars_photo{index + 1}.jpg was saved!!!")
        else:
            logging.error('Photo request issue:', response.status_code)
else:
    logging.error('Request issue:', response.status_code)

