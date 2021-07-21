import requests

#Gets the request URL
url = ('https://newsapi.org/v2/top-headlines?country=us&apiKey=f37c44a1fbb348cea7579fd9ba26e78e')

#Gets the information and converts it into JSON format
response = requests.get(url)
r = response.json()

#Prints where the news article is from and prints a description
counter = 1
i = 0
while counter < 11:
    if r.get('articles')[i].get('description') != None:
        print(str(r.get('articles')[i].get('source').get('name')) + ":\n" + str(r.get('articles')[i].get('description')) + "\n")
        counter += 1
    i += 1

#Access key: f37c44a1fbb348cea7579fd9ba26e78e
