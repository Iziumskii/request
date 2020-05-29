import requests

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def read_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        file = f.read()
    return file


def save_translate(path, text):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


def translate_it(rpath, wpath, from_lang, to_lang='ru'):
    params = {
        'key': API_KEY,
        'text': read_text(rpath),
        'lang': '{}-{}'.format(from_lang, to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    resalt = ''.join(json_['text'])
    save_translate(wpath, resalt)


if __name__ == '__main__':
    translate_it('DE.txt', 'DE-RU.txt', 'de')
