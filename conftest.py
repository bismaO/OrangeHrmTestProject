import pytest
from BaseSeleniumFramework.Driver import Driver


@pytest.fixture
def driver():
    driver = Driver().get_driver()
    yield driver
    Driver().quit_driver()