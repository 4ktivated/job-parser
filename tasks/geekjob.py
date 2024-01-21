from bs4 import BeautifulSoup
from selenium import webdriver
import time

def geekjob_jobs(text : str):
    func_base = []
    url = "https://geekjob.ru/vacancies?qs=" + text
    browser = webdriver.Chrome()
 

    browser.get(url)
    time.sleep(2)
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')

  
    for vacaincie in soup.find_all('li', class_ = 'collection-item avatar'):
        name = vacaincie.find('p', class_ = 'truncate company-name').text.strip()
        title = vacaincie.find('p', class_ = 'truncate vacancy-name').text.strip()
        info = str(vacaincie.find('div', class_ = 'info')).replace('<br/>', ' ')[18:-7]
        #при использованнии text тег br стирает пробел между городом и потенциаяльной зарплатой
        if not info:
            info = 'Не указанно'
        link = 'https://geekjob.ru' + vacaincie.a['href']
        
    
        func_base.append({'lang': text, 'Title': title, 'Company': name, 'URL': link, 'Salary': 'из-за источника все даныне в инфо', 'Info': info})
    return func_base



# text = 'python'
# print(geekjob_jobs(text))


