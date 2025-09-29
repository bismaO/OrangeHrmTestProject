import pytest
from BaseSeleniumFramework.Driver import Driver


@pytest.fixture
def driver():
    driver = Driver("chrome").get_driver()
    yield driver
    driver.quit_driver()