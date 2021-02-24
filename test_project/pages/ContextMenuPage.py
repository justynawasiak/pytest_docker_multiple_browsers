class ContextMenuPage:
    page_url = 'https://the-internet.herokuapp.com/context_menu'

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.page_url)

    def get_page_source(self):
        return self.driver.page_source
