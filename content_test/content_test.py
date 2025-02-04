import os
import requests

# Definition of the API address
api_address = os.environ.get('API_ADDRESS', 'localhost')
api_port = os.environ.get('API_PORT', '8000')

def content_test():
    print("============================")
    print("    Content Test")
    print("============================")

    # Define test sentences
    sentences = [
        {'username': 'alice', 'sentence': 'hello shitty world', 'expected_sentiment': 'negative'},
        {'username': 'alice', 'sentence': 'hello wonderful world', 'expected_sentiment': 'positive'}
    ]

    for sentence in sentences:
        # Prepare the request parameters
        params = {
            'username': sentence['username'],
            'password': 'wonderland',
            'sentence': sentence['sentence']
        }

        # Make a GET request to the /v1/sentiment endpoint
        response = requests.get(f'http://{api_address}:{api_port}/v1/sentiment', params=params)

        # Check if the request was successful
        if response.status_code == 200:
            # Extract sentiment score from the response
            sentiment_score = response.json().get('score')

            # Determine sentiment based on sentiment score
            sentiment = 'positive' if sentiment_score > 0 else 'negative'

            # Check if the calculated sentiment matches the expected sentiment
            if sentiment == sentence['expected_sentiment']:
                test_status = 'SUCCESS'
            else:
                test_status = 'FAILURE'

            # Print test results
            print(f"Request done at '/v1/sentiment'")
            print(f"| username='{sentence['username']}'")
            print(f"| sentence='{sentence['sentence']}'")
            print(f"Expected sentiment = {sentence['expected_sentiment']}")
            print(f"Actual sentiment = {sentiment}")
            print(f"==> {test_status}")

            # Print output to log file if LOG environment variable is set
            if os.environ.get('LOG') == '1':
                with open('api_test.log', 'a') as file:
                    file.write(f"\n\n============================\n    Content Test\n============================\n")
                    file.write(f"Request done at '/v1/sentiment'\n")
                    file.write(f"| username='{sentence['username']}'\n")
                    file.write(f"| sentence='{sentence['sentence']}'\n")
                    file.write(f"Expected sentiment = {sentence['expected_sentiment']}\n")
                    file.write(f"Actual sentiment = {sentiment}\n")
                    file.write(f"==> {test_status}\n")
        else:
            print(f"Failed to fetch data from the API. Status code: {response.status_code}")

if __name__ == "__main__":
    content_test()
