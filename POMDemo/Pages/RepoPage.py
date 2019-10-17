class RepoPage:

    def __init__(self, driver):
        self.driver = driver
        self.issue_btn_Xpath = "//nav/span[2]/a"

    def issue(self):
        self.driver.find_element_by_xpath(self.issue_btn_Xpath).click()
