from VK import VkPhoto
from YandexDisk import YandexDisk


if __name__ == '__main__':
    vk_client = VkPhoto(input('Введите токен Вконтакте: '))
    vk_client.get_photos(input('Укажите количество фото, которое нужно выгрузить: '))
