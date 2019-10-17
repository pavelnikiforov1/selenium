from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By



class NewIssuePage:

    def __init__(self, driver):
        self.driver = driver
        self.title_textbox_by_id = "issue_title"
        self.body_textbox_by_id = "issue_body"
        self.submit_btn_Xpath = "//*[@id='new_issue']/div/div[1]/div/div/div["  "2]/button"
        self.dropdown_Xpath = "//header/div/details/summary/img"
        self.logout_btn = "/html/body/div[1]/header/div[5]/details/details-menu/form/button"

    def write_title(self, title):
        self.driver.find_element_by_id(self.title_textbox_by_id).send_keys(title)

    def write_body(self, body):
        self.driver.find_element_by_id(self.body_textbox_by_id).send_keys(body)

    def click_btn(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(ec.element_to_be_clickable((By.XPATH, self.submit_btn_Xpath)))
        element.click()

    def log_out(self):
        self.driver.find_element_by_xpath(self.dropdown_Xpath).click()
        self.driver.find_element_by_xpath(self.logout_btn).click()
