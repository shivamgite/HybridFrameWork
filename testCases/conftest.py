from selenium import webdriver
import pytest
from datetime import datetime

# pytest -s -v -n=2 testCases/test_Login.py --browser chrome      //parallel run test case//-n=2 we have two testcase
# parallel testing plugin required /// pytest-xdist
# pytest -s -v  testCases/test_Login.py --browser chrome     //to pass browser name from command line

def screenshot(driver):
    driver.save_screenshot ( f"C:\\Users\\sgite\\PycharmProjects\\HybridFrameWork\\Screenshots\\{datetime.now().strftime('%Y:%m:%d_%H:%M:%S')}.png" )


@pytest.fixture ()
def setup(browser):
    if browser=="chrome":
        driver = webdriver.Chrome ( executable_path="C:\\Users\sgite\PycharmProjects\HybridFrameWork\Drivers\chromedriver\chromedriver.exe" )
    elif browser=="firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\sgite\PycharmProjects\HybridFrameWork\Drivers\geckodriver\geckodriver.exe")
    elif browser=="ie":
        driver = webdriver.Ie(executable_path="C:\\Users\\sgite\PycharmProjects\HybridFrameWork\Drivers\IEDriverServer\IEDriverServer.exe")
    elif browser == None:
        driver = webdriver.Chrome (
            executable_path="C:\\Users\\sgite\PycharmProjects\HybridFrameWork\Drivers\chromedriver\chromedriver.exe" )
    driver.maximize_window ()
    driver.implicitly_wait ( 10 )
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request) :
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata['1. Project name'] = 'nop Commerce'
    config._metadata['2. Module name'] = 'Customers'
    config._metadata['3. Platform name'] = 'Windows-10'
    config._metadata['4. Python version'] = '3.9.0'
    config._metadata['5. Tester name'] = 'Shivam Gite'




@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop ( "Plugins", None )
    metadata.pop ( "Packages", None )
    metadata.pop ( "Platform", None )
    metadata.pop ( "Python", None )
