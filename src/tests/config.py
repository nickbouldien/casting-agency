import os

# test tokens for each role
assistant_bearer_token = os.environ.get('ASSISTANT_TEST_TOKEN')

director_bearer_token = os.environ.get('DIRECTOR_TEST_TOKEN')

producer_bearer_token = os.environ.get('PRODUCER_TEST_TOKEN')


headers = {'content-type': "application/json"}


# Create auth headers for each user (role)
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
