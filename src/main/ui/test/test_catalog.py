from src.main.ui.steps.catalog_steps import CatalogSteps
from src.main.ui.conftest import auth_page


def test_count_catalog(auth_page):
    steps = CatalogSteps(auth_page)
    assert steps.get_products_count() == 6

def test_sorted_by_name_a_to_z(auth_page):
    steps = CatalogSteps(auth_page)

    steps.sort_items("az")
    assert steps.get_product_name() == sorted(steps.get_product_name())

    steps.sort_items("za")
    assert steps.get_product_name() == sorted(steps.get_product_name(), reverse=True)

def test_sort_by_price(auth_page):
    steps = CatalogSteps(auth_page)

    steps.sort_items("lohi")
    assert steps.get_product_prices() == sorted(steps.get_product_prices())

    steps.sort_items("hilo")
    assert steps.get_product_prices() == sorted(steps.get_product_prices(), reverse=True)

def test_add_to_cart(auth_page):
    steps = CatalogSteps(auth_page)
    steps.add_to_cart("Sauce Labs Bike Light")
    assert steps.get_cart_count() == 1

def test_add_and_remove_onesie(auth_page):
    steps = CatalogSteps(auth_page)
    steps.add_to_cart("Sauce Labs Onesie")
    assert steps.get_cart_count() == 1

    steps.remove_from_cart("Sauce Labs Onesie")
    assert steps.get_cart_count() == 0

def test_product_details_onesie(auth_page):
    steps = CatalogSteps(auth_page)
    name, price, detail_name, detail_price = steps.open_product_details("Sauce Labs Onesie")
    assert name == detail_name
    assert price == detail_price

def test_product_details_jacket(auth_page):
    steps = CatalogSteps(auth_page)
    steps.add_to_cart("Sauce Labs Fleece Jacket")

    name, price, detail_name, detail_price = steps.open_product_details("Sauce Labs Fleece Jacket")
    assert name == detail_name
    assert price == detail_price

def test_remove_item_from_catalog_red(auth_page):
    steps = CatalogSteps(auth_page)
    steps.remove_from_cart("Test.allTheThings() T-Shirt (Red)")

def test_remove_item_from_catalog_onesie(auth_page):
    steps = CatalogSteps(auth_page)
    steps.remove_from_cart("Sauce Labs Onesie")


