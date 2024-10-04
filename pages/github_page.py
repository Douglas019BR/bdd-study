from page_objects import PageObject, PageElement
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CSS_MAP = {
    "login_button": 'a[href="/login"]',
    "search_button": 'button[data-action="click:qbsearch-input#handleExpand"]',
    "first_result_link": 'div[data-testid="results-list"] a',
}

ID_MAP = {
    "user_name_text_field": "login_field",
    "password_text_field": "password",
    "text_field": "query-builder-test",
}


class GithubPage(PageObject):
    login_button = PageElement(css=CSS_MAP["login_button"])
    user_name_text_field = PageElement(id_=ID_MAP["user_name_text_field"])
    password_text_field = PageElement(id_=ID_MAP["password_text_field"])
    search_button = PageElement(css=CSS_MAP["search_button"])
    text_field = PageElement(id_=ID_MAP["text_field"])
    first_result_link = PageElement(css=CSS_MAP["first_result_link"])

    def login(self, user_name: str, password: str) -> None:
        self.login_button.click()
        WebDriverWait(self.w, 10).until(
            EC.element_to_be_clickable((By.ID, ID_MAP["user_name_text_field"]))
        )
        self.user_name_text_field.send_keys(user_name)
        self.password_text_field.send_keys(password)
        assert self.user_name_text_field.get_attribute("value") == user_name
        assert self.password_text_field.get_attribute("value") == password
        self.password_text_field.send_keys(Keys.ENTER)

    def search_buttom_click(self) -> None:
        WebDriverWait(self.w, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, CSS_MAP["search_button"]))
        )
        self.search_button.click()

    def search_for_term(self, term: str) -> None:
        WebDriverWait(self.w, 10).until(
            EC.element_to_be_clickable((By.ID, ID_MAP["text_field"]))
        )
        self.text_field.send_keys(term)
        assert self.text_field.get_attribute("value") == term
        self.text_field.send_keys(Keys.ENTER)

    def open_first_result(self) -> None:
        WebDriverWait(self.w, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, CSS_MAP["first_result_link"]))
        )
        self.first_result_link.click()
        from time import sleep

        sleep(2)  # waiting to load the page


if __name__ == "__main__":
    from credentials import user_name, password
    from time import sleep

    try:
        driver = webdriver.Chrome()
        driver.get("https://github.com/")
        page = GithubPage(driver)
        page.login(user_name, password)
        sleep(1)  # To visualize the result
        page.search_buttom_click()
        sleep(1)  # To visualize the result
        page.search_for_term("Douglas019BR/bdd-study")
        page.open_first_result()
        sleep(1)  # To visualize the result
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
