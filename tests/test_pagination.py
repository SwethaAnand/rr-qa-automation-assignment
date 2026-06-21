from pages.home_page import HomePage
from selenium.webdriver.support.ui import WebDriverWait


def test_next_page(setup):

    home = HomePage(setup)

    current_page = home.get_current_page()

    home.click_next_page()

    WebDriverWait(setup, 10).until(
        lambda d: home.get_current_page() != current_page
    )

    assert int(home.get_current_page()) == int(current_page) + 1