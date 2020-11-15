import pytest
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def init_driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    web_driver = webdriver.Chrome(options=options, executable_path='C:\\Users\\ibei\\PycharmProjects\\Python_Serv-U\\chromedriver')
    request.cls.driver = web_driver
    web_driver.implicitly_wait(5)
    yield
    web_driver.close()


#@pytest.fixture(scope="class")
#def do_login(username, password):
#    init_driver()
# driver.do_send_keys(USERNAME_BOX, username)
#    do_send_keys(PASSWORD, password)
#    do_click(LOGIN_BUTTON)

#TODO add new fixture for login per 1 class, and fixture logount per 1 class an the end
#TODO fixture to check failed test or not and to screen with timestamp to folder screenshot
