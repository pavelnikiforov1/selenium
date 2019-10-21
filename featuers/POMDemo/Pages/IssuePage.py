class IssuePage:

    def __init__(self, driver):
        self.driver = driver
        self.issue_btn_linkTxt = "New issue"

    def new_issue(self):
        self.driver.find_element_by_link_text(self.issue_btn_linkTxt).click()
