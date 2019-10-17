class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.dropdown_btn_Xpath = "/html/body/div[1]/header/div[7]/details/summary/img"
        self.my_repo_linkTxt = "Your repositories"

    def click_on_dropdown(self):
        self.driver.find_element_by_xpath(self.dropdown_btn_Xpath).click()

    def click_on_repos(self):
        self.driver.find_element_by_link_text(self.my_repo_linkTxt).click()
