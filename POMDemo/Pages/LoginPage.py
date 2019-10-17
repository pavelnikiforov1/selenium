class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_name = "login"
        self.password_textbox_name = "password"
        self.login_btn_name = "commit"

    def enter_username(self, username):
        self.driver.find_element_by_name(self.username_textbox_name).clear()
        self.driver.find_element_by_name(self.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_textbox_name).clear()
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(password)

    def click(self):
        self.driver.find_element_by_name(self.login_btn_name).click()
