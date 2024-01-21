import requests
from bs4 import BeautifulSoup as BS
import lxml
import selenium


def habr_jobs(text):
    func_base = []
    habr_url = 'https://career.habr.com/vacancies?q='+ text +'&qid=3&type=all'
    
    response = requests.get(habr_url, timeout=10)

    soup = BS(response.text, "lxml")

    if response.status_code == 200:
        for box in soup.find_all('div', class_ = 'vacancy-card__info'):
            name = box.div.div.text
            title = box.find('div', class_ = 'vacancy-card__title').text
            stack = box.find('div', class_ = 'vacancy-card__skills').text
            link = 'https://career.habr.com' + box.a['href']

            if box.find('div', class_ = 'vacancy-card__salary').text:
                salary = box.find('div', class_ = 'vacancy-card__salary').text
            else:
                salary = 'Не указанна'
            func_base.append({'lang': text, 'Title': title, 'Company': name, 'URL': link, 'Salary': salary, 'Info': stack})
        return func_base

# example = 'python'
# print(habr_jobs(example))
