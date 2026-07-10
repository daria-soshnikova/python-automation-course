import requests
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get("https://api.github.com", params = payload)
print(f"Статус ответа: {response.status_code}")
print(f"Заголовок Content-Type: {response.headers['Content-Type']}")

response2 = requests.get("https://api.github.com/search/repositories", params={"q": "selenium"})
print(f"Статус: {response2.status_code}")
print(response2.url)