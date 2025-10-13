import os
import requests
from requests.exceptions import RequestException as e

"""Взяв інший ендпоінт із зображенням в респонсі, так як той, що вказаний для домашки
не працює, віддає 404 помилку"""

url = 'https://api.nasa.gov/planetary/apod'
params = {'api_key': 'DEMO_KEY'}

def save_image_from_response(url, params):
    file_dir = 'images'
    os.makedirs(file_dir, exist_ok=True)

    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise e(f"Request failed with status {response.status_code} and message: {response.content}")
    data = response.json()

    image_url = data.get('url')
    if not image_url:
        raise ValueError("No image URL found in the response")

    filename = os.path.join(file_dir, os.path.basename(image_url))
    img_response = requests.get(image_url)
    if img_response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(img_response.content)
    else:
        raise e(f"Image download failed with status {img_response.status_code} and message: {img_response.content}")