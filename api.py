import requests

url = "https://uc3.netiapps.net/api/authenticate"  # Use actual API endpoint

try:
    response = requests.post(url, data={"username": "DUM39995", "password": "123456789"})
    response.raise_for_status()  # Raises an HTTPError for bad responses
    print(response.json())
except requests.exceptions.HTTPError as e:
    if response.status_code == 404:
        print(f"404 Not Found: The endpoint {url} is not valid.")
    else:
        print(f"HTTP error occurred: {e}")
except Exception as e:
    print(f"Other error occurred: {e}")
