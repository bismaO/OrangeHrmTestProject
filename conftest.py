import pytest
from BaseSeleniumFramework.Driver import Driver


@pytest.fixture
def driver():
    driver = Driver().get_driver()
    yield driver
    driver.quit_driver()