from behave import *
from selenium import webdriver

from featuers.POMDemo.Pages.HomePage import HomePage
from featuers.POMDemo.Pages.LoginPage import MainPage as LoginPage
from featuers.POMDemo.Pages.ReposPage import RepoSPage
from featuers.POMDemo.Pages.RepoPage import RepoPage
from featuers.POMDemo.Pages.IssuePage import IssuePage
from featuers.POMDemo.Pages.NewIssuePage import NewIssuePage

use_step_matcher("re")

driver = None


@given("I am on git login page")
def step_impl(context):
    driver = webdriver.Chrome("C:/Users/pavel/PycharmProjects/seleniom/drivers/chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    context.driver = driver
    context.driver.get("https://github.com/login")


@when("I performe login")
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.enter_username("pavelnikiforov1")
    login_page.enter_password("pavelniki787")
    login_page.click()


@step("I hit the right tab and the repository button")
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.click_on_dropdown()
    home_page.click_on_repos()


@step("I hit the chosen repository")
def step_impl(context):
    repos_page = RepoSPage(context.driver)
    repos_page.go_to_repo()


@step("I hit the issue tab")
def step_impl(context):
    repo_page = RepoPage(context.driver)
    repo_page.issue()


@step("I hit the New Issue button")
def step_impl(context):
    issue_page = IssuePage(context.driver)
    issue_page.new_issue()


@step("i type a issue title and body and performe logout")
def step_impl(context):
    new_issue_page = NewIssuePage(context.driver)
    new_issue_page.write_title("my 6th selenium issue title")
    new_issue_page.write_body("my 6th selenium issue body ")
    new_issue_page.click_btn()
    new_issue_page.log_out()
