from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects import PageObject, PageElement
from selenium import webdriver

NAME_MAP = {"text_field": "q", "i_m_luck_button": "btnI"}


class GoogleSearchPage(PageObject):
    text_field = PageElement(name=NAME_MAP["text_field"])
    i_m_luck_button = PageElement(name=NAME_MAP["i_m_luck_button"])

    def search_for_term(self, term: str) -> None:
        self.text_field.send_keys(term)
        assert self.text_field.get_attribute("value") == term

    def search_with_i_m_luck(self) -> None:
        WebDriverWait(self.w, 10).until(
            EC.element_to_be_clickable((By.NAME, NAME_MAP["i_m_luck_button"]))
        )
        self.i_m_luck_button.click()


if __name__ == "__main__":
    from time import sleep

    driver = webdriver.Chrome()
    driver.get("http://google.com")
    page = GoogleSearchPage(driver)
    page.search_for_term("github")
    page.search_with_i_m_luck()
    sleep(1)  # To visualize the result
    driver.quit()
