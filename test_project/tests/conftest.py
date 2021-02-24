import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(params=['chrome', 'firefox'], scope='class')
def get_driver(request):
    if request.param == "firefox":
        driver = webdriver.Remote('http://selenium:4444/wd/hub', DesiredCapabilities.FIREFOX)
    else:
        driver = webdriver.Remote('http://selenium:4444/wd/hub', DesiredCapabilities.CHROME)
    request.cls.driver = driver

    yield driver
    driver.quit()

