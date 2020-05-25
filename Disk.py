import requests

API_KEY = 'AgAAAAAW7ysGAADLW3UW9AZUokols341Kq_3KII'
URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'


def url_it(path):
    headers = {"Authorization": "OAuth AgAAAAAW7ysGAADLW3UW9AZUokols341Kq_3KII"}
    params = {
        'path': path,
        # 'overwrite': overwrite,
        # 'fields': fields,
    }

    response = requests.get(URL, headers=headers, params=params)
    json = response.json()
    print(json)
    return ''.join(json['href'])


def upload(path):
    url_1 = url_it(path)

    params = {
        'path': path,
        # 'fields': fields,
    }

    response = requests.put(url_1, params=params)
    print(response)


upload('DE-RU.txt')
