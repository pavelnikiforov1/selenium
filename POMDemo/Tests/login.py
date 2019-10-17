from selenium import webdriver

import unittest

from POMDemo.Pages.HomePage import HomePage
from POMDemo.Pages.LoginPage import MainPage as LoginPage
from POMDemo.Pages.ReposPage import RepoSPage
from POMDemo.Pages.RepoPage import RepoPage
from POMDemo.Pages.IssuePage import IssuePage
from POMDemo.Pages.NewIssuePage import NewIssuePage


class GoogleSearch(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:/Users/pavel/PycharmProjects/seleniom/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test01_login(self):

        self.driver.get("https://github.com/login")
        login_page = LoginPage(self.driver)
        login_page.enter_username("pavelnikiforov1")
        login_page.enter_password("pavelniki787")
        login_page.click()

    def test02_home_page(self):
        home_page = HomePage(self.driver)
        home_page.click_on_dropdown()
        home_page.click_on_repos()

    def test03_repos_page(self):

        repos_page = RepoSPage(self.driver)
        repos_page.go_to_repo()

    def test04_repo_page(self):
        repo_page = RepoPage(self.driver)
        repo_page.issue()

    def test05_issue_page(self):
        issue_page = IssuePage(self.driver)
        issue_page.new_issue()

    def test06_new_issue_page(self):
        new_issue_page = NewIssuePage(self.driver)
        new_issue_page.write_title("my 6th selenium issue title")
        new_issue_page.write_body("my 6th selenium issue body ")
        new_issue_page.click_btn()
        new_issue_page.log_out()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")


if __name__ == '__main__':
    unittest.main()
