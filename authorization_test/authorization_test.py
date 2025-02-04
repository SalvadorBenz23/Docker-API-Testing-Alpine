import os
import requests

# Definition of the API address
api_address = os.environ.get('API_ADDRESS', 'localhost')
api_port = os.environ.get('API_PORT', '8000')

def authorization_test():
    print("============================")
    print("    Authorization Test")
    print("============================")

    # Define test users and their permissions
    users = [
        {'username': 'bob', 'password': 'builder', 'version': 'v1'},
        {'username': 'alice', 'password': 'wonderland', 'version': 'v1'},
        {'username': 'alice', 'password': 'wonderland', 'version': 'v2'}
    ]

    for user in users:
        # Prepare the request parameters
        params = {
            'username': user['username'],
            'password': user['password']
        }

        # Make a GET request to the /v1/sentiment and /v2/sentiment endpoints
        for version in ['v1', 'v2']:
            response = requests.get(f'http://{api_address}:{api_port}/{version}/sentiment', params=params)

            # Display the test results
            if response.status_code == 200:
                test_status = 'SUCCESS'
            else:
                test_status = 'FAILURE'

            print(f"Request done at '/{version}/sentiment'")
            print(f"| username='{user['username']}'")
            print(f"| password='{user['password']}'")
            print(f"Expected result = 200")
            print(f"Actual result = {response.status_code}")
            print(f"==> {test_status}")

            # Print output to log file if LOG environment variable is set
            if os.environ.get('LOG') == '1':
                with open('api_test.log', 'a') as file:
                    file.write(f"\n\n============================\n    Authorization Test\n============================\n")
                    file.write(f"Request done at '/{version}/sentiment'\n")
                    file.write(f"| username='{user['username']}'\n")
                    file.write(f"| password='{user['password']}'\n")
                    file.write(f"Expected result = 200\n")
                    file.write(f"Actual result = {response.status_code}\n")
                    file.write(f"==> {test_status}\n")

if __name__ == "__main__":
    authorization_test()
