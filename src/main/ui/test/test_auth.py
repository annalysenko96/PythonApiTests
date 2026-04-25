from playwright.sync_api import expect
from src.main.ui.pages.catalog_page import CatalogPage
from src.main.ui.steps.login_steps import LoginSteps
from src.main.ui.pages.login_page import LoginPage

def test_auth(page):
    steps = LoginSteps(page)
    steps.open_login_page().login("standard_user","secret_sauce")
    catalog_page = CatalogPage(page)
    assert catalog_page.get_products_count() > 0, "Ожидаем товары на странице каталога"

def test_auth_blocked(page):
    steps = LoginSteps(page)
    steps.open_login_page().login("locked_out_user","secret_sauce")
    error_text = steps.login_page.get_error_text()
    assert "locked out" in error_text, "Ожидаем сообщение о заблоченом пользаке"

def test_logout(auth_page):
    catalog = CatalogPage(auth_page)
    assert catalog.get_products_count() > 0
    catalog.logout()
    expect(auth_page).to_have_url(LoginPage.URL)

def test_login_visual(auth_visual_page):
    catalog = CatalogPage(auth_visual_page)
    assert catalog.get_products_count() > 0
    catalog.logout()
    expect(auth_visual_page).to_have_url(LoginPage.URL)
