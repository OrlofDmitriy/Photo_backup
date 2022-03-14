import requests
import json
import time
from tqdm import tqdm
from datetime import datetime


class VkPhoto:

    def __init__(self, token):
        self.params = {
            'access_token': token,
            'v': '5.131'
        }

    def _user(self):
        inquiry = int(input('Введите 1 если запрос по имени пользователя. Введите 2 - если по ID: '))

        if inquiry == 1:
            user_id = input('Введите имя пользователя: ')
            user_params = {
                'user_ids': user_id,
            }
            res = requests.get('https://api.vk.com/method/users.get', params={**self.params, **user_params})
            users = res.json()['response'][0]['id']
        elif inquiry == 2:
            user_id = input('Введите ID: ')
            users = user_id
        else:
            print('Нет такой команды!')

        return users

    def get_photos(self, count=5):
        photos_params = {
            'owner_id': self._user(),
            'album_id': 'profile',
            'photo_sizes': 1,
            'rev': 0,
            'extended': 'likes',
            'count': count
        }
        res = requests.get('https://api.vk.com/method/photos.get', params={**self.params, **photos_params})
        photos = res.json()['response']['items']
        likes = {}
        data_for_json = []
        photo_list = []

        for el in photos:
            likes.setdefault(el['likes']['count'], 0)
            likes[el['likes']['count']] += 1
        for el in tqdm(photos):
            photo_data = []
            like = el['likes']['count']
            date = datetime.now().date()
            if likes[like] > 1:
                name = f'{like}_{date}'
            else:
                name = like
            photo_url = el['sizes'][-1]['url']
            _type = el['sizes'][-1]['type']
            data_for_json.append({'file_name': f'{name}.jpg', 'size': _type})
            photo_data.append(str(name))
            photo_data.append(photo_url)
            photo_list.append(photo_data)
            time.sleep(1)

        with open('photos.json', 'w') as file:
            json.dump(data_for_json, file, ensure_ascii=False, indent=2)

        return photo_list
