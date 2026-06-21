from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    popular = (By.LINK_TEXT, "Popular")
    trend = (By.LINK_TEXT, "Trend")
    newest = (By.LINK_TEXT, "Newest")
    top_rated = (By.LINK_TEXT, "Top rated")
    search_box = (By.XPATH, "//*[@id='root']/div/div/div/div/div/div")
    type_dropdown = (By.XPATH, "//div/p[contains(text(), 'Type')]//parent::div/div[1]/div")
    selected_page = (By.XPATH,"//div[@id='react-paginate']/ul/li[@class='selected']")
    next_page = (By.XPATH,"//div[@id='react-paginate']/ul/li[@class='selected']/following-sibling::li[1]")
    previous_page = (By.XPATH,"//div[@id='react-paginate']/ul/li[@class='selected']/preceding-sibling::li[1]")

    def click_popular(self):
        self.driver.find_element(*self.popular).click()

    def click_trend(self):
        self.driver.find_element(*self.trend).click()

    def click_newest(self):
        self.driver.find_element(*self.newest).click()

    def click_top_rated(self):
        self.driver.find_element(*self.top_rated).click()

    def search_movie(self, movie_name):
        self.driver.find_element(*self.search_box).clear()
        self.driver.find_element(*self.search_box).send_keys(movie_name)

    def get_search_text(self):
        return self.driver.find_element(*self.search_box).get_attribute("value")

    def click_type_dropdown(self):
        self.driver.find_element(*self.type_dropdown).click()


    def select_movie(self):
        self.driver.find_element(*self.type_dropdown).click()
        self.driver.switch_to.active_element.send_keys("Movie")
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)

    def select_tv_show(self):
        self.driver.find_element(*self.type_dropdown).click()
        self.driver.switch_to.active_element.send_keys("TV Shows")
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)

    def click_next_page(self):
        self.driver.find_element(*self.next_page).click()

    def click_previous_page(self):
        self.driver.find_element(*self.previous_page).click()

    def get_current_page(self):
        return self.driver.find_element(*self.selected_page).text