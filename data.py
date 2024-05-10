import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
new_data = response.json()

question_data = new_data["results"]
