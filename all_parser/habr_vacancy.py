import requests
from bs4 import BeautifulSoup as BS
import lxml


def habr_job(text):
    habr_url = 'https://career.habr.com/vacancies?q='+ text +'&qid=3&type=all'
    
    response = requests.get(habr_url).text

    soup = BS(response, "lxml")

    for box in soup.find_all('div', class_ = 'vacancy-card__info'):
        
        name = box.div.div.text
        title = box.find('div', class_ = 'vacancy-card__title').text
        stack = box.find('div', class_ = 'vacancy-card__skills').text
        link = 'https://career.habr.com/' + box.a['href']
        
        if box.find('div', class_ = 'vacancy-card__salary').text:
            salary = box.find('div', class_ = 'vacancy-card__salary').text
        else:
            salary = 'Не указанна'

        
        print(f'Title: {title}\nCompany: {name}\nURL: {link}\nSalary: {salary}\nStack: {stack}')
        print()


text = 'python'      
habr_job(text)