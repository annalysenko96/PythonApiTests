
from main.api.requests.credit_repay_requester import CreditRepayRequester
from main.api.steps.base_steps import BaseSteps


class CreditRepaySteps(BaseSteps):
    def credit_repay(self, credit_repay_data, response_spec = None):
        response = CreditRepayRequester(
            request_spec = self.request_spec,
            response_spec = response_spec,
        ).post(credit_repay_data)
        return response


