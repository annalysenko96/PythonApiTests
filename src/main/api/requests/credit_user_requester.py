from http import HTTPStatus
import requests
from requests import Response
from src.main.api.models.credit_get_response import CreditGetResponse
from src.main.api.models.credit_get_request import CreditGetRequest
from src.main.api.requests.requester import Requester


class CreditUserRequester(Requester):
    def post(self,credit_request:CreditGetRequest) -> CreditGetResponse | Response:
        url =f"{self.base_url}/credit/request"
        response = requests.post(
            url = url,
            json = credit_request.model_dump(),
            headers = self.headers
        )
        self.response_spec(response)
        if response.status_code in [HTTPStatus.CREATED]:
            return CreditGetResponse (**response.json())
        return response
