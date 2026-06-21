from pages.home_page import HomePage

def test_tv_show_filter(setup):

    home = HomePage(setup)

    home.select_tv_show()

def test_tv_movie_filter(setup):

    home = HomePage(setup)

    home.select_movie()