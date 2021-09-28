"""
1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев
для конкретного пользователя, сохранить JSON-вывод в файле *.json.
"""
import requests
import json

user_name = 'octocat'  # имя пользователя
url = f"https://api.github.com/users/{user_name}/repos"  # url для доступа к репозиториям пользователя
file_name = 'for_task_1.json'  # имя файла для сохранения вывода

response = requests.get(f"{url}?type=owner")
data = json.loads(response.text)

for repo in data:
    print(repo['name'])  # вывод названий репозиториев пользователя

with open(file_name, "w") as new_file:
    json.dump(data, new_file, indent=2)  # сохранение json-вывода в файл
