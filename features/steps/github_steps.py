from time import sleep
from behave import when
from credentials import user_name, password
from pages.github_page import GithubPage


@when("faço o login com as credenciais do arquivo de configuração")
def step_impl(context):
    page = GithubPage(context.driver)
    page.login(user_name, password)


@when("clico na busca do github")
def step_impl(context):
    page = GithubPage(context.driver)
    page.search_buttom_click()


@when("busco o seguinte texto {termo}")
def step_impl(context, termo):
    page = GithubPage(context.driver)
    page.search_for_term(termo)


@when("clico no primeiro resultado")
def step_impl(context):
    page = GithubPage(context.driver)
    page.open_first_result()
