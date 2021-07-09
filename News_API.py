import requests

url = ('https://newsapi.org/v2/top-headlines?country=us&apiKey=f37c44a1fbb348cea7579fd9ba26e78e')

response = requests.get(url)
r = response.json()
for i in range(10):
    print(r.get('articles')[i].get('source').get('name') + ":\n\t" + r.get('articles')[i].get('description') + "\n")

#Access key: f37c44a1fbb348cea7579fd9ba26e78e