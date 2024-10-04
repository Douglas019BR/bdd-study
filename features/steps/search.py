from behave import when, then

from pages.search_page import GoogleSearchPage


@when('preencho o campo de busca com o texto {termo}')
def step_impl(context, termo):
    page = GoogleSearchPage(context.driver)
    page.search_for_term(termo)

@when('clico em estou com sorte')
def step_impl(context):
    page = GoogleSearchPage(context.driver)
    page.search_with_i_m_luck()

@then('devo ser redirecionado para a página {site}')
def step_impl(context, site):
    assert site == context.driver.current_url
