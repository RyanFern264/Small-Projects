import requests

response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()
data = response.json()["results"]

question_data = []

for i in range(0, len(data)):
    question_data.append(data[i])
print(question_data)
