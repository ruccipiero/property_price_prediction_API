import requests

url = "https://property-price-prediction-api.onrender.com/"

#headers = {"accept": "application/json"}
predict = "predict"
response = requests.get(url+predict)

print(response.text)