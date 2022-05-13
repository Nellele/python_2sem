import requests
from bs4 import BeautifulSoup

def animals(animal):
    link = 'https://ru.wikipedia.org/wiki/' + animal
    response = requests.get(link).text
    document = BeautifulSoup(response, features='html.parser')
    table = document.find('table')
    td = table.find('td', {'class': 'plainlist'})
    div = td.find_all('div', {'class': 'ts-Taxonomy-rang-row'})
    for i in range(len(div)):
        word = div[i].find_all('div')
        if word[0].text == 'Класс:':
            return word[1].text


print(animals('Осьминог'))
print(animals('Львы'))
