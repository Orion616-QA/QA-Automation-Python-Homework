import requests
from requests.exceptions import RequestException as e

BASE_URL = "http://127.0.0.1:8080"
TEST_FILE = "/Users/macbookpro13/Downloads/welcome.jpg"
filename = 'welcome.jpg'

def upload_image():
    with open(TEST_FILE, "rb") as f:
        files = {"image": f}
        response = requests.post(f"{BASE_URL}/upload", files=files)
    if response.status_code == 201:
        return response.json().get("image_url")
    else:
        raise e(f"Request failed with status {response.status_code} and message: {response.content}")


def get_image(filename):
    headers = {"Content-Type": "text"}
    response = requests.get(f"{BASE_URL}/image/{filename}", headers=headers)

    if response.status_code == 200:
        data = response.json()
        image_url = data.get("url")
        return image_url
    else:
        raise e(f"Request failed with status {response.status_code} and message: {response.content}")

def delete_image(filename):
    response = requests.delete(f"{BASE_URL}/delete/{filename}")
    if response.status_code == 200:
        pass
    else:
        raise e(f"Request failed with status {response.status_code} and message: {response.content}")