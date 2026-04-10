from typing import Any, List

from main.api.steps.credit_repay_steps import CreditRepaySteps
from src.main.api.steps.admin_steps import AdminSteps
from src.main.api.steps.account_steps import AccountSteps
from src.main.api.steps.credit_steps import CreditSteps
from src.main.api.steps.user_steps import UserSteps


class ApiManager:
    def __init__(self,create_obj:List[Any]):
        self.create_obj = create_obj
        self.admin_steps = AdminSteps(create_obj)
        self.user_steps = UserSteps(create_obj)


    def account_steps(self, request_spec):
        return AccountSteps(self.create_obj, request_spec)

    def credit_steps(self, request_spec):
        return CreditSteps(self.create_obj, request_spec)

    def credit_repay_steps(self, request_spec):
        return CreditRepaySteps(self.create_obj, request_spec)
