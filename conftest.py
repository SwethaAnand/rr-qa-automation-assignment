import pytest
from utilities.driver_factory import get_driver


@pytest.fixture()
def setup():
    driver = get_driver()
    driver.get("https://tmdb-discover.surge.sh/")

    yield driver

    driver.quit()