"""
2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.
"""
import requests
import json

# https://developers.gfycat.com - Authentication Model : OAuth 2

# 1 step - Get a client id. All you need is a gfycat account.
client_id = "client_id"
client_secret = "client_secret"
username = "username"
password = "password"

# 2 step - to get an access token
url = "https://api.gfycat.com/v1/oauth/token"
payload = {
    "grant_type": "password",
    "client_id": client_id,
    "client_secret": client_secret,
    "scope": '',
    "username": username,
    "password": password
  }
response = requests.post(url, data=json.dumps(payload))
data = json.loads(response.text)
token = data["access_token"]

# 3 step - try to use API service for "retrieve a list of all reaction gif categories"
url = "https://api.gfycat.com/v1/reactions/populated"
key = {"Authorization": f"Bearer {token}"}
response = requests.get(f"{url}?gfyCount=1", key)
data = json.loads(response.text)

# 4 step - save in file
file_name = 'for_task_2.json'
with open(file_name, "w") as new_file:
    json.dump(data, new_file, indent=2)
