
import requests
import json

url = 'http://127.0.0.1:5000/json'
#files = {'file': open('C:\\Users\\Comme\\Desktop\\demo.json', 'rb')}
with open('C:\\Users\\Comme\\Desktop\\demo.json', 'r',encoding='utf8')as f:
    print(f)
    my_data = json.load(f)
print(my_data)
#print(files)
r = requests.post(url,data=my_data)
print(r)
print(r.text)
