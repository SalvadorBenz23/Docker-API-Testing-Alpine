import os
import requests

# Definition of the API address
api_address = os.environ.get('API_ADDRESS', 'localhost')
api_port = os.environ.get('API_PORT', '8000')

def authentication_test():
    print("============================")
    print("    Authentication Test")
    print("============================")

    # Prepare the request parameters
    params = {
        'username': 'alice',
        'password': 'wonderland'
    }

    # Make a GET request to the /permissions endpoint
    response = requests.get(f'http://{api_address}:{api_port}/permissions', params=params)

    # Display the test results
    if response.status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'

    print(f"Request done at '/permissions'")
    print(f"| username='alice'")
    print(f"| password='wonderland'")
    print(f"Expected result = 200")
    print(f"Actual result = {response.status_code}")
    print(f"==> {test_status}")

    # Print output to log file if LOG environment variable is set
    if os.environ.get('LOG') == '1':
        with open('api_test.log', 'a') as file:
            file.write(f"\n\n============================\n    Authentication Test\n============================\n")
            file.write(f"Request done at '/permissions'\n")
            file.write(f"| username='alice'\n")
            file.write(f"| password='wonderland'\n")
            file.write(f"Expected result = 200\n")
            file.write(f"Actual result = {response.status_code}\n")
            file.write(f"==> {test_status}\n")

if __name__ == "__main__":
    authentication_test()
