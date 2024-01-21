import requests
from bs4 import BeautifulSoup as BS
import lxml
from selenium import webdriver  #это тут для парсера с OZON, но егоя не доделал

#не работает


def vk_jobs(text : str):
    func_base = []
    url = 'https://team.vk.company/vacancy/?specialty=&town=&tag=&search=' + text
    
    response = requests.get(url)
    soup = BS(response.text, 'lxml')
    
    if response.status_code == 200:
        
        for vacancy in soup.find_all('a', class_ = 'result-item js-result-list-item'):
            title = vacancy.find('h3', class_ = 'title-block').text.strip()
            project = vacancy.find('div', class_ = 'result-item-unit').text.strip()
            city_type = vacancy.find('div', class_ = 'result-item-place').text.strip()
            link = 'https://team.vk.company' + vacancy['href']

            func_base.append({'lang': text, 'Title': title, 'Company': project, 'URL': link, 'Salary': 'Не указанна', 'Info': city_type})

        return func_base
    
    # else:
    #     print('Sorry this language is not support :(')


# def ozon_jobs(text):
#     url = 'https://job.ozon.ru/vacancy/?query=' + text
#     # browser = webdriver.Chrome()
    
#      with open('html_ozon.html', 'w', encoding='utf-8') as r:
#          browser.get(url)
#          html = browser.page_source
#          soup = BS(html, 'lxml')
#          r.write(html)
#     response = requests.get(url).text
#     soup = BS(response, 'lxml')
#     print(soup)

#     for vacancy in soup.find_all('div', class_= 'hr'):
#         link  = 'https://job.ozon.ru/' + vacancy['href']
#         title = vacancy.find('h6', class_ = 'result__title').text
#         city = vacancy.find('span').text
#         project = vacancy.find('span').text
#         print(f'Title: {title}\nProject: {project}\nCity: {city}\nLink: {link}\n')

text = 'python'
# #ozon_job(text)
print(vk_jobs(text))