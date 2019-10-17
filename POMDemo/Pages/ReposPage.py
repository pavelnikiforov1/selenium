class RepoSPage:

    def __init__(self, driver):
        self.driver = driver
        self.choosen_repo_linkTxt = "Spring-Angular-CouponS"

    def go_to_repo(self):
        self.driver.find_element_by_link_text(self.choosen_repo_linkTxt).click()
