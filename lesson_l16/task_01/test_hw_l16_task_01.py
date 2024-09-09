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
        team_lead_developer: TeamLead = (
            TeamLead("Vasja", 20_000, "QA", "Python", 6))

        logging.info("Step 2: Create expected result data.")
        expected_result = {
            'name': 'Vasja',
            'salary': 20000,
            'department': 'QA',
            'programming_language': 'Python',
            'team_size': 6
        }

        logging.info("Step 3: Verify expected result data.")
        logging.info(f"Substep 3.1: Verify that \"name\" is {expected_result['name']}.")
        assert_that(team_lead_developer.get_name()).is_equal_to(expected_result['name'])
        logging.info(f"Substep 3.2: Verify that \"salary\" is {expected_result['salary']}.")
        assert_that(team_lead_developer.get_salary()).is_equal_to(expected_result['salary'])
        logging.info(f"Substep 3.3: Verify that \"department\" is {expected_result['department']}.")
        assert_that(team_lead_developer.get_department()).is_equal_to(expected_result['department'])
        logging.info(f"Substep 3.4: Verify that \"programming_language\" is {expected_result['programming_language']}.")
        assert_that(team_lead_developer.get_programming_language()).is_equal_to(expected_result['programming_language'])
        logging.info(f"Substep 3.5: Verify that \"team_size\" is {expected_result['team_size']}.")
        assert_that(team_lead_developer.get_team_size()).is_equal_to(expected_result['team_size'])
