from behave import step, when
from selenium import webdriver


@step('que eu esteja com o browser aberto')
def open_browser(context):
    if context.driver_path:
        context.driver = webdriver.Chrome(executable_path=context.driver_path)
    else:
        context.driver = webdriver.Chrome()

@when('acesso o {url}')
def step_impl(context, url):
    if url.startswith("http://") or url.startswith("https://"):
        fixed_url = url
    else:
        fixed_url = f"https://{url}"
    context.driver.get(fixed_url)
