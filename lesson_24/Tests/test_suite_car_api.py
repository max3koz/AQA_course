import logging
import pytest

from assertpy import assert_that


class TestSuiteCarAPI:
    @pytest.mark.parametrize("api_url, expected_gty_cars", [("/cars?limit=0", 0),
                                                            ("/cars?limit=1", 1),
                                                            ("/cars?limit=25", 25),
                                                            ("/cars?limit=26", 25)],
                             indirect=True)
    def test_get_car_list_by_limit(self, expected_gty_cars, api_url, authorization, setup_logging):
        logging.info("Test START")
        logging.info("Verify that authorization is PASS")
        response = authorization.get(api_url)
        assert_that(response.status_code).is_equal_to(200)

        logging.info("Verify the quantity of car in the expected cars list")
        assert_that(len(response.json())).is_equal_to(expected_gty_cars)


    @pytest.mark.parametrize("api_url, sorted_by, expected_car_list", [("/cars?sort_by=brand&limit=5",
                                                                        "brand",
                                                                        ["Acura", "Audi", "BMW", "Bugatti", "Chevrolet"]),
                                                                       ("/cars?sort_by=engine_volume&limit=5",
                                                                        "engine_volume",
                                                                        ["Tesla", "Nissan", "Honda", "Hyundai", "Audi"]),
                                                                       ("/cars?sort_by=price&limit=5",
                                                                        "price",
                                                                        ["Chevrolet", "Hyundai", "Honda", "Kia", "Ford"]),
                                                                       ("/cars?sort_by=year&limit=5",
                                                                        "year",
                                                                        ["Ford", "Honda", "Toyota", "Subaru", "BMW"])],
                             indirect=True)
    def test_get_car_by_parameters(self, api_url, sorted_by, expected_car_list, authorization, setup_logging):
        logging.info("Test START")
        logging.info("Verify that authorization is PASS")
        response = authorization.get(api_url)
        assert_that(response.status_code).is_equal_to(200)

        logging.info("Verify the expected cars list")
        result = response.json()
        car_list = []
        for item in result:
            car_list.append(item["brand"])
        assert_that(car_list).is_equal_to(expected_car_list)
