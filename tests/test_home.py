from pages.home_page import HomePage


def test_popular_category(setup):

    home = HomePage(setup)

    home.click_popular()

    assert "popular" in setup.current_url.lower()


def test_trend_category(setup):

    home = HomePage(setup)

    home.click_trend()

    assert "trend" in setup.current_url.lower()


def test_newest_category(setup):

    home = HomePage(setup)

    home.click_newest()

    assert "new" in setup.current_url.lower()


def test_top_rated_category(setup):

    home = HomePage(setup)

    home.click_top_rated()

    assert "top" in setup.current_url.lower()