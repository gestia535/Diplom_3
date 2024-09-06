import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from data import BASE_URL
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.order_history_page import OrderHistoryPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.user_account_page import UserAccountPage


@pytest.fixture(params=[webdriver.Firefox, webdriver.Chrome], ids=['firefox', 'chrome'], scope="function")
def driver(request):
    driver_class = request.param
    if driver_class == webdriver.Chrome:
        options = Options()
        options.add_argument('--incognito')
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1280, 720)
    elif driver_class == webdriver.Firefox:
        firefox_options = webdriver.FirefoxOptions()
        profile = FirefoxProfile()
        profile.set_preference("browser.privatebrowsing.autostart", True)
        firefox_options.profile = profile
        driver = webdriver.Firefox(options=firefox_options)
        driver.set_window_size(1280, 720)
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    main_page_obj = MainPage(driver)
    return main_page_obj


@pytest.fixture
def user_acc_page(driver):
    user_acc_page = UserAccountPage(driver)
    return user_acc_page


@pytest.fixture
def pass_recovery_page(driver):
    pass_recovery = PasswordRecoveryPage(driver)
    return pass_recovery


@pytest.fixture
def feed_page(driver):
    feed_page_obj = FeedPage(driver)
    return feed_page_obj


@pytest.fixture
def order_history_page(driver):
    order_history_page = OrderHistoryPage(driver)
    return order_history_page

# @pytest.fixture
# def login(user_acc_page):
#     login = user_acc_page.login()
#     return login

# def generate_user_credentials():
#     email = email_generator()
#     password = password_generator()
#     name = create_random_name()
#     return email, password, name
#
#
# @pytest.fixture
# def create_new_user_and_delete():
#     payload_cred = {
#         'email': email_generator(),
#         'password': password_generator(),
#         'name': create_random_name()
#     }
#     response = requests.post(REGISTER_URL, data=payload_cred)
#     response_body = response.json()
#
#     yield payload_cred, response_body
#
#     access_token = response_body['accessToken']
#     requests.delete(DELETE_URL, headers={'Authorization': access_token})
#
#
# @pytest.fixture
# def create_user_and_order_and_delete(create_new_user_and_delete):
#     access_token = create_new_user_and_delete[1]['accessToken']
#     headers = {'Authorization': access_token}
#     payload = {'ingredients': [
#         '61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa6c',
#         '61c0c5a71d1f82001bdaaa76', '61c0c5a71d1f82001bdaaa79'
#     ]}
#     response_body = requests.post(ORDER_URL, data=payload, headers=headers)
#
#     yield access_token, response_body
#     requests.delete(DELETE_URL, headers={'Authorization': access_token})


# @pytest.fixture
# def set_user_tokens(driver, create_new_user_and_delete):
#     driver.get(Urls.base_url)
#     user_data = create_new_user_and_delete[1]
#     access_token = user_data.get('accessToken')
#     refresh_token = user_data.get('refreshToken')
#     driver.execute_script(f'window.localStorage.setItem("accessToken", "{access_token}");')
#     driver.execute_script(f'window.localStorage.setItem("refreshToken", "{refresh_token}");')



# @pytest.fixture
# @allure.title('Фикстура передает в драйвер токены созданного пользователя')
# def set_user_tokens(driver, create_new_user_and_delete):
#     driver.get(Urls.base_url)
#     user_data = create_new_user_and_delete[1]
#     access_token = user_data.get('accessToken')
#     refresh_token = user_data.get('refreshToken')
#     driver.execute_script(f'window.localStorage.setItem("accessToken", "{access_token}");')
#     driver.execute_script(f'window.localStorage.setItem("refreshToken", "{refresh_token}");')
