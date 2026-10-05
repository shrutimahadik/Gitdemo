import datetime
import os


import pytest
from selenium import webdriver
driver=None



def pytest_addoption(parser):
    parser.addoption(
        "--browsername", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture(scope="function")



def browserinstance():
    global driver
    options = webdriver.ChromeOptions()

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
    )

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    yield driver

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    "extend pytest plugin to take and embed screenshot in html report whenever test:param item"

    pytest_html=item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra=getattr(report,'extra',[])
    if report.when == "call" or report.when=='setup':
        xfail =hasattr(report,'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'reports')


            file_name=os.path.join(reports_dir,report.nodeid.replace("::","_")+".png")
            print("file name is " + file_name)
            _capture_screenshot(file_name)
            if file_name:
                html='<div><img src="%s" alt="screenshot"style="width:304px;height:228px;" '\
                     'onclick="window.open(this.src)" align="right"/></div>'%file_name
                extra.append(pytest_html.extras.html(html))
        report.extra=extra

def  _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)


