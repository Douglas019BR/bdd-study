from behave import when

from pages.google_search_page import GoogleSearchPage


@when("preencho o campo de busca com o texto {termo}")
def step_impl(context, termo):
    page = GoogleSearchPage(context.driver)
    page.search_for_term(termo)


@when("clico em estou com sorte")
def step_impl(context):
    page = GoogleSearchPage(context.driver)
    page.search_with_i_m_luck()
