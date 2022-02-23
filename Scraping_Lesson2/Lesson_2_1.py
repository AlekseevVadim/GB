"""
Необходимо собрать информацию о вакансиях на вводимую должность
(используем input или через аргументы получаем должность) с сайтов HH(обязательно)
и/или Superjob(по желанию). Приложение должно анализировать несколько страниц сайта
(также вводим через input или аргументы). Получившийся список должен содержать в себе минимум:
- Наименование вакансии.
- Предлагаемую зарплату (разносим в три поля: минимальная и максимальная и валюта. цифры преобразуем к цифрам).
- Ссылку на саму вакансию.
- Сайт, откуда собрана вакансия.
По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение).
Структура должна быть одинаковая для вакансий с обоих сайтов.
Общий результат можно вывести с помощью dataFrame через pandas. Сохраните в json либо csv.
"""

import requests
import json
import pandas as pd
from bs4 import BeautifulSoup as bs

url = 'https://hh.ru'
area = 1  # Значение для фильтра по региону - Москва
text = 'Data Engineer'  # Наименование должности
text_formatted = "+".join([word.lower() for word in text.split()])
page = 0  # Номер страницы с результатами поиска

params = {'clusters': 'true',
          'area': area,
          'ored_clusters': 'true',
          'enable_snippets': 'true',
          'salary': '',
          'text': text_formatted,
          'page': page}
# Просмотр заголовка User-Agent браузера chrome - chrome://version/
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

vacancies = []  # итоговый список вакансий

while True:
    params['page'] = page
    # сбор ссылки для правильного отображения символа '+' в params (вместо %2B)
    url_req = url + '/search/vacancy?' + '&'.join(['='.join((x, str(params[x]))) for x in params])
    response = requests.get(url_req, headers=headers)
    # print(response.url) - просмотр итогового запроса
    soup = bs(response.text, 'html.parser')
    div_vacancies = soup.findAll('div', attrs={'class': 'vacancy-serp-item'})
    if not div_vacancies:
        break

    for vacancy in div_vacancies:
        vacancy_data = {}  # словарь с данными о вакансии
        first_block = vacancy.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})
        name = first_block.text  # наименование должности
        link = first_block['href']  # ссылка на вакансию
        second_block = vacancy.find('span', attrs={'data-qa': 'vacancy-serp__vacancy-compensation'})
        if second_block is not None:
            salary_text = second_block.text.split()
            salary = {}  # зарплата
            if salary_text[0] == 'от':
                salary_min = int(''.join(salary_text[1:-1]))
                salary_max = None
            elif salary_text[0] == 'до':
                salary_max = int(''.join(salary_text[1:-1]))
                salary_min = None
            else:
                i_stop = salary_text.index('–')
                salary_min = int(''.join(salary_text[:i_stop]))
                salary_max = int(''.join(salary_text[i_stop + 1:-1]))
            salary_value = salary_text[-1]
            salary['min'] = salary_min
            salary['max'] = salary_max
            salary['value'] = salary_value
        else:
            salary = None
        third_block = vacancy.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-employer'})
        employer_name = ' '.join(third_block.text.split())  # наименование работодателя
        employer_link = third_block['href']  # ссылка на страницу работодателя
        employer_address = vacancy.find('div', attrs={'data-qa': 'vacancy-serp__vacancy-address'}).text  # адрес работы

        vacancy_data['name'] = name
        vacancy_data['link'] = link
        vacancy_data['salary'] = salary
        vacancy_data['employer'] = {'name': employer_name, 'address': employer_address, 'link': url + employer_link}
        vacancies.append(vacancy_data)
    page += 1

# вывод количества найденных вакансий
print(len(vacancies))

# запись полученных данных в файл
file_name = 'HW_2_task_1.json'
with open(file_name, "w", encoding='utf-8') as new_file:
    json.dump(vacancies, new_file, ensure_ascii=False, indent=2)

# вывод полученных данных с помощью dataFrame через pandas
data = pd.read_json('D:\PROFESSOR\geekbrains\Методы сбора и обработки данных из сети Интернет\HW\Lesson 2\HW_2_task_1.json')
print(data.head(10))
