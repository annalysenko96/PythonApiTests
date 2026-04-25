from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.requests.create_account_requester import CreateAccountRequester
from src.main.api.requests.deposit_account_requester import DepositAccountRequester
from src.main.api.requests.transfer_account_requester import TransferAccountRequester
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps


class AccountSteps(BaseSteps):
    def create_account(self, response_spec = None):
        response = CreateAccountRequester(
            request_spec= self.request_spec,
            response_spec= response_spec or  ResponseSpecs.request_created()
        ).post()
        self.created_obj.append(response)
        return response

    def create_account_deposit(self,deposit_data, response_spec=ResponseSpecs.request_ok()):
        response = DepositAccountRequester(
        request_spec=self.request_spec,
        response_spec=response_spec
        ).post(deposit_data)
        return response
    def create_account_deposit_invalid(self,deposit_data, response_spec=ResponseSpecs.request_bad()):
        response = DepositAccountRequester(
        request_spec=self.request_spec,
        response_spec=response_spec
        ).post(deposit_data)
        return response

    def transfer_account(self, transfer_data, response_spec=ResponseSpecs.request_ok()):
        response = TransferAccountRequester(
            request_spec=self.request_spec,
            response_spec=response_spec
        ).post(transfer_data)
        return response

    def transfer_account_invalid(self, transfer_data, response_spec=ResponseSpecs.request_bad()):
        response = TransferAccountRequester(
            request_spec=self.request_spec,
            response_spec=response_spec
        ).post(transfer_data)
        return response
