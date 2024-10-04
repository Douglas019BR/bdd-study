from page_objects import PageObject, PageElement
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GithubPage(PageObject):
    login_button = PageElement(css='a[href="/login"]')
    user_name_text_field = PageElement(id_="login_field")
    password_text_field = PageElement(id_="password")
    search_button = PageElement(css='button[data-action="click:qbsearch-input#handleExpand"]')
    text_field = PageElement(id_="query-builder-test")
    first_result_link = PageElement(css='div[data-testid="results-list"] a')

    def login(self, user_name: str, password: str) -> None:
        self.login_button.click()
        WebDriverWait(self.w, 10).until(EC.element_to_be_clickable((By.ID, "login_field")))
        self.user_name_text_field.send_keys(user_name)
        self.password_text_field.send_keys(password)
        assert self.user_name_text_field.get_attribute("value") == user_name
        assert self.password_text_field.get_attribute("value") == password
        self.password_text_field.send_keys(Keys.ENTER)

    def search_buttom_click(self) -> None:
        WebDriverWait(self.w, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-action="click:qbsearch-input#handleExpand"]')))
        self.search_button.click()

    def search_for_term(self, term: str) -> None:
        WebDriverWait(self.w, 10).until(EC.element_to_be_clickable((By.ID, "query-builder-test")))
        self.text_field.send_keys(term)
        assert self.text_field.get_attribute("value") == term
        self.text_field.send_keys(Keys.ENTER)

    def open_first_result(self) -> None:
        WebDriverWait(self.w, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div[data-testid="results-list"] a')))
        self.first_result_link.click()
        from time import sleep
        sleep(1)

    

if __name__ == "__main__":
    from credentials import user_name,password
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
        import ipdb;ipdb.set_trace()
        sleep(1)  # To visualize the result
        page.open_first_result()
        sleep(1)  # To visualize the result
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()