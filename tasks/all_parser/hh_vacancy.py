import requests

def hh_jobs_perm(text : str):
    func_base = []
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": text,
        "area": [72, 2, 1, 3],  # Specify the desired area ID (72:Perm, 2:SPB, 1:MSC, 3:EKB)
        "per_page": 100,  # Number of vacancies per page
    }

    response = requests.get(url, params=params, timeout=10)

    if response.status_code == 200:
        data = response.json()
        vacancies = data.get("items", [])
        for vacancy in vacancies:
            
            vacancy_title = vacancy.get("name")
            vacancy_url = vacancy.get("alternate_url")
            company_name = vacancy.get("employer", {}).get("name")
            experience = vacancy.get('experience', {}).get('name')
            
            #Костыль с зарплатой из-за неправильного форматирования
            if vacancy.get('salary', {}) and vacancy.get('salary', {}).get("from") and vacancy.get('salary', {}).get('to'):
               salary_from = vacancy.get('salary', {}).get("from")
               salary_to = vacancy.get('salary', {}).get('to')
               salary = f'{salary_from} - {salary_to}'
            elif vacancy.get('salary', {}) and not vacancy.get('salary', {}).get("from"):
                salary = vacancy.get('salary', {}).get('to')
            elif vacancy.get('salary', {}) and not vacancy.get('salary', {}).get("to"):
                salary = vacancy.get('salary', {}).get('from')
            else:
                salary = 'Не указанна'
                
            func_base.append({'lang': text, 'Title': vacancy_title, 'Company': company_name, 'URL': vacancy_url, 'Salary': salary, 'Info': experience})
            
        return(func_base)
    # else:
    #     print(f"Request failed with status code: {response.status_code}")
 