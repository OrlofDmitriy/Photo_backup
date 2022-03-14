import requests
from tqdm import tqdm
import time


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def create_directory(self, name_directory='Photo_backup'):
        directory_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': name_directory, 'overwrite': 'true'}
        requests.put(directory_url, headers=headers, params=params)
        return name_directory

    def upload_file_to_disk(self, photo_list):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        name_directory = self.create_directory()

        for file in tqdm(photo_list):
            params = {'path': f'{name_directory}/{file[0]}.jpg', 'url': file[1]}
            response = requests.post(url, headers=headers, params=params)
            response.raise_for_status()
            if response.status_code == 201:
                print('Success')
            time.sleep(1)
