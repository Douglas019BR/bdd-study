from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects import PageObject, PageElement
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class GoogleSearchPage(PageObject): 
  text_field = PageElement(name='q')
  i_m_luck_button = PageElement(name='btnI')
  search_button = PageElement(name='btnK')


  def search_for_term(self, term: str) -> None:
    self.text_field.send_keys(term)
    assert self.text_field.get_attribute('value') == term

  def search_with_i_m_luck(self) -> None:
    WebDriverWait(self.w, 10).until(
            EC.element_to_be_clickable((By.NAME, 'btnI'))
        )
    self.i_m_luck_button.click()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://google.com")
    page = GoogleSearchPage(driver)
    page.search_for_term("github")
    page.search_with_i_m_luck()
    sleep(1) # To visualize the result
    driver.quit()


