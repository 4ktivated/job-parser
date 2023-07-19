import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def parse_geekjob(text):
    
    url = "https://geekjob.ru/vacancies?qs=" + text
    browser=webdriver.Chrome()
    
    with open('data.html', 'r+', encoding='utf-8') as r:
        browser.get("https://geekjob.ru/vacancies?qs=" + text)
        html = browser.page_source
        soup = BeautifulSoup(html, 'lxml')
        r.write(html)
  
    for vacaincie in soup.find_all('li', class_ = 'collection-item avatar'):
        name = vacaincie.find('p', class_ = 'truncate company-name').text.strip()
        title = vacaincie.find('p', class_ = 'truncate vacancy-name').text.strip()
        info = vacaincie.find('div', class_ = 'info').text
        if not info:
            info = 'Не указанно'
        for i in range(len(info)):
            if info[i].isdigit():
                info = info[:i-1] + '\n      ' + info[i:]
                break
        link = 'https://geekjob.ru/' + vacaincie.a['href']
        
    
        print(f'Title: {title}\nCompany: {name}\nURL: {link}\nInfo: {info}')
        print()


text = 'python'
parse_geekjob(text)


