from behave import step, when, then
from selenium import webdriver


@step("que eu esteja com o browser aberto")
def open_browser(context):
    if context.driver_path:
        context.driver = webdriver.Chrome(executable_path=context.driver_path)
    else:
        context.driver = webdriver.Chrome()


@when("acesso o {url}")
def step_impl(context, url):
    if url.startswith("http://") or url.startswith("https://"):
        fixed_url = url
    else:
        fixed_url = f"https://{url}"
    context.driver.get(fixed_url)


@then("devo ser redirecionado para a página {site}")
def step_impl(context, site):
    print(context.driver.current_url)
    print(site)
    assert site == context.driver.current_url
