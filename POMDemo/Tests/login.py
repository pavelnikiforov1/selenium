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

    def test_git(self):
        driver = self.driver

        driver.get("https://github.com/login")

        login_page = LoginPage(driver)
        login_page.enter_username("pavelnikiforov1")
        login_page.enter_password("pavelniki787")
        login_page.click()

        home_page = HomePage(driver)
        home_page.click_on_dropdown()
        home_page.click_on_repos()

        repos_page = RepoSPage(driver)
        repos_page.go_to_repo()

        repo_page = RepoPage(driver)
        repo_page.issue()

        issue_page = IssuePage(driver)
        issue_page.new_issue()

        new_issue_page = NewIssuePage(driver)
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
