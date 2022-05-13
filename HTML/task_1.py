import requests
from bs4 import BeautifulSoup

def courses(year, season):
    l, course = [], []
    str_year = str(year)
    if len(str_year) == 4:
        link = 'http://students.iposov.spb.ru/' + str_year[2:] + season + '/'
    else:
        link = 'http://students.iposov.spb.ru/' + str_year + season + '/'
    response = requests.get(link).text
    document = BeautifulSoup(response, features='html.parser')
    section = document.find('section', {'class': 'main-content'})
    ul = section.find('ul')
    ulul = ul.find_all('ul')
    for i in range(len(ulul)):
        l.extend(ulul[i].find_all('li'))
    for i in range(len(l)):
        course.append(l[i].find('a').text)
    return course


year = 2022
season = 'spring'
y = 19
print(courses(year, season))
print(courses(y, season))
