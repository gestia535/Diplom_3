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
