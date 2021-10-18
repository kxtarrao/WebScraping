import requests
from bs4 import BeautifulSoup

while True:
    name = input('Input Celebrity Name: ')
    URL = 'https://en.wikipedia.org/wiki/' + name.title().replace(" ", "_")

    request = requests.get(URL)
    if request.status_code == 200:
        page = BeautifulSoup(request.text, 'html.parser')
    else:
        print('[ERROR] Page not found')
        page = None

    if page:
        info = {
            'Given Name':   'nickname',
            'DOB':          'bday',
            'Age':          'noprint ForceAgeToShow',
            'Nationality':  'infobox-data category',
            'Occupation':   'infobox-data role',
        }

        for key in info.keys():
            if page.find(class_=info[key]):
                info[key] = page.find(class_=info[key]).text
            else:
                info[key] = None

        if info['Age']:
            info['Age'] = ''.join(filter(str.isdigit, info['Age']))

        for key in info:
            print(f'{key}: {info[key]}')
