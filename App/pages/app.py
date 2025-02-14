from App.pages.base_page import BasePage


class APP(BasePage):
    def start(self):
        self.driver.launch_app()

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def quit(self):
        self.driver.quit()
