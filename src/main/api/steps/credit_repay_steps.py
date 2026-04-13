
from main.api.requests.credit_repay_requester import CreditRepayRequester
from main.api.specs.response_specs import ResponseSpecs
from main.api.steps.base_steps import BaseSteps


class CreditRepaySteps(BaseSteps):
    def credit_repay(self, credit_repay_data, response_spec = ResponseSpecs.request_ok()):
        response = CreditRepayRequester(
            request_spec = self.request_spec,
            response_spec = response_spec,
        ).post(credit_repay_data)
        return response

    def credit_repay_invalid_bad(self, credit_repay_data, response_spec = ResponseSpecs.request_bad()):
        response = CreditRepayRequester(
            request_spec = self.request_spec,
            response_spec = response_spec,
        ).post(credit_repay_data)
        return response

    def credit_repay_invalid_ue(self, credit_repay_data, response_spec = ResponseSpecs.request_unprocessable_entity()):
        response = CreditRepayRequester(
            request_spec = self.request_spec,
            response_spec = response_spec,
        ).post(credit_repay_data)
        return response


