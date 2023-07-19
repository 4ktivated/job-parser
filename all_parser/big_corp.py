import requests
from bs4 import BeautifulSoup as BS
import lxml
from selenium import webdriver


text = 'python'

def vk_jobs(text : str):
    url = 'https://team.vk.company/vacancy/?specialty=&town=&tag=&search=' + text
    
    response = requests.get(url).text
    soup = BS(response, 'lxml')
    
    for vacancy in soup.find_all('a', class_ = 'result-item js-result-list-item'):
        title = vacancy.find('h3', class_ = 'title-block').text.strip()
        project = vacancy.find('div', class_ = 'result-item-unit').text.strip()
        city_type = vacancy.find('div', class_ = 'result-item-place').text.strip()
        link = 'https://team.vk.company' + vacancy['href']
        
        print(f'Title: {title}\nProject: {project}\nCity and Type work: {city_type}\nLink: {link}\n')



# def ozon_jobs(text):
#     url = 'https://job.ozon.ru/vacancy/?tech=' + text.capitalize()
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


#ozon_job(text)
vk_jobs(text)