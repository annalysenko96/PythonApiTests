import allure
from playwright.sync_api import Page
from src.main.ui.pages.cheсkout_page import CheckoutPage



class CheckoutSteps:
    def __init__(self,page:Page):
        self.page = page
        self.checkout = CheckoutPage(page)

    @allure.step("Начинаем с Checkout: {last_name}, {first_name},{postal_code}")
    def start_checkout(self,last_name:str,first_name:str,postal_code:str):
        self.checkout.start_checkout(last_name,first_name,postal_code)
        return self

    @allure.step("Завершаем Checkout")
    def finish_checkout(self):
        self.checkout.finish_checkout()
        return self

    @allure.step("Получаем текст ошибки на Checkout")
    def get_error_text(self) ->str:
        return self.checkout.get_error_text()

    @allure.step("Получаем сумму товаров после Checkout")
    def get_item_total_after_continue(self) ->float:
        return self.checkout.get_item_total_after_continue()

