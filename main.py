from VK import VkPhoto
from YandexDisk import YandexDisk


if __name__ == '__main__':
    vk_client = VkPhoto(input('Введите токен Вконтакте: '))
    ya_client = YandexDisk(input('Введите токен Яндекс Диска: '))
    ya_client.upload_file_to_disk(vk_client.get_photos(input('Укажите количество фото, которые нужно загрузить: ')))
    print('Фото загружены!')
