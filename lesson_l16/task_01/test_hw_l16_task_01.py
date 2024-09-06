import logging

from assertpy import assert_that
from logging import config
from lesson_l16.task_01.team_lead import TeamLead

logging.config.fileConfig('logging_config.ini')
logging.getLogger('sampleLogger')


class TestSuite:

    def test_case_with_valid_data_positive(self):
        logging.info("The test case was run:")
        logging.info("Step 1: Create the \"Team lead\" employess with valid data "
                     "in \"name\", \"salary\", \"department\" and \"team_size\" fields.")
        team_lead_developer: TeamLead = TeamLead("Vasja", 20_000, "QA", 6)

        logging.info("Step 2: Create expected result data.")
        expected_result = {
            'name': 'Vasja',
            'salary': 20_000,
            'department': 'QA',
            'team_size': 6
        }

        logging.info("Step 3: Verify expected result data.")
        assert_that(team_lead_developer.__dict__).is_equal_to(expected_result)
