import os
# from ..utils import create_bearer_token_payload, get_bearer_token


# auth0_domain = os.environ.get('AUTH0_DOMAIN')
# audience = os.environ.get('AUDIENCE')
# default_grant_type = "client_credentials"
# domain = f'https://{auth0_domain}'

# assistant data
# assistant_client_id = os.environ.get('ASSISTANT_CLIENT_ID')
# assistant_client_secret = os.environ.get('ASSISTANT_CLIENT_SECRET')
assistant_bearer_token = os.environ.get('ASSISTANT_TEST_TOKEN')

# director data
# director_client_id = os.environ.get('DIRECTOR_CLIENT_ID')
# director_client_secret = os.environ.get('DIRECTOR_CLIENT_SECRET')
director_bearer_token = os.environ.get('DIRECTOR_TEST_TOKEN')

# producer data
# producer_client_id = os.environ.get('PRODUCER_CLIENT_ID')
# producer_client_secret = os.environ.get('PRODUCER_CLIENT_SECRET')
producer_bearer_token = os.environ.get('PRODUCER_TEST_TOKEN')


headers = {'content-type': "application/json"}

# payload = {
#     "client_id": "{}",
#     "client_secret": "{}",
#     "audience": "{}",
#     "grant_type": "client_credentials"
# }

# assistant_payload = create_bearer_token_payload(
#                                                 assistant_client_id,
#                                                 assistant_client_secret,
#                                                 audience,
#                                                 default_grant_type
#                                             )
#
#
# director_payload = create_bearer_token_payload(
#                                                 director_client_id,
#                                                 director_client_secret,
#                                                 audience,
#                                                 default_grant_type
#                                             )
#
# producer_payload = create_bearer_token_payload(
#                                                 producer_client_id,
#                                                 producer_client_secret,
#                                                 audience,
#                                                 default_grant_type
#                                             )


# assistant_bearer_token = get_bearer_token(domain, assistant_payload, headers)
# director_bearer_token = get_bearer_token(domain, director_payload, headers)
# producer_bearer_token = get_bearer_token(domain, producer_payload, headers)

# Create auth headers for each user
assistant_header = {"Authorization": f"Bearer {assistant_bearer_token}"}
director_header = {"Authorization": f"Bearer {director_bearer_token}"}
producer_header = {"Authorization": f"Bearer {producer_bearer_token}"}

if __name__ == '__main__':
    print('---------------')
    print('tests/config.py')
    print(f'assistant_bearer_token => {assistant_bearer_token}')
    print(f'director_bearer_token => {director_bearer_token}')
    print(f'producer_bearer_token => {producer_bearer_token}')
    print('---------------')
