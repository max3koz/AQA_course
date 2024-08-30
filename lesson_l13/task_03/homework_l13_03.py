import xml.etree.ElementTree as ET
import  logging

from pathlib import Path

path = Path("/home/mtrykoz/Projects/AQA_course/lesson_l13/task_03/work_with_xml")

logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S"
        )

tree = ET.parse(f"{path}/groups.xml")
root = tree.getroot()

for group in root.findall('group'):
    timing_exbytes_element = group.find('timingExbytes')
    if timing_exbytes_element is not None:
        incoming_field = timing_exbytes_element.find('incoming')
        if incoming_field is not None:
            logging.info(f"Group: {group.find('number').text}, incoming: {incoming_field.text}")
        else:
            logging.info(f"Group: {group.find('number').text}, \"incoming\" tag doesn`t exist in groupe")
    else:
        logging.info(f"Group: {group.find('number').text}, \'timingExbytes\" tag doesn`t exist in groupe")
