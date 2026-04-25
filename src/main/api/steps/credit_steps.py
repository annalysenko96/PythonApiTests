from src.main.api.models.credit_get_request import CreditGetRequest
from src.main.api.requests.credit_user_requester import CreditUserRequester
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps


class CreditSteps(BaseSteps):
    def credit_data(self, account_id, amount,term_months, response_spec = ResponseSpecs.request_created()):
        request_data = CreditGetRequest(
            accountId = account_id,
            amount = amount,
            termMonths=term_months
        )

        response = CreditUserRequester(
            request_spec = self.request_spec,
            response_spec = response_spec or ResponseSpecs.request_created()

        ).post(request_data)
        return response

    def credit_data_indalid(self, account_id, amount,term_months, response_spec = ResponseSpecs.request_bad()):
        request_data = CreditGetRequest(
            accountId = account_id,
            amount = amount,
            termMonths=term_months
        )

        response = CreditUserRequester(
            request_spec = self.request_spec,
            response_spec = response_spec or ResponseSpecs.request_created()

        ).post(request_data)
        return response