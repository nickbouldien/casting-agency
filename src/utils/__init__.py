from typing import Dict, Union
import requests
import http.client
import json


def check_valid_age(age: Union[str, int]) -> bool:
    if type(age) is str:
        try:
            age = int(age)
        except Exception as e:
            print('error casting the age to an int ', e)
            return False

    return False if age < 0 else True


def get_bearer_token(domain: str, payload, headers) -> str:
    # conn = http.client.HTTPSConnection("docs.python.org")
    print('domain', domain)
    print('payload', payload)
    print('headers', headers)

    response = requests.post(domain, json=payload, headers=headers)

    print("get_bearer_token response ", response)

    if response:
        print('response.json()', response.json())
        print("headers: ", response.headers)
    else:
        print('An error has occurred.')

    # TODO
    return ""


def create_bearer_token_payload(
                                client_id: str,
                                client_secret: str,
                                audience: str,
                                grant_type: str = "client_credentials"
                            ) -> Dict[str, str]:
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "audience": audience,
        "grant_type": grant_type
    }

    return payload
