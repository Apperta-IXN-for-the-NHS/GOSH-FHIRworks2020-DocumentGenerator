import requests 

data = requests.get('http://127.0.0.1:5002/p/eunice/').json()

#print(data)
for dat in data:
    print(dat)

