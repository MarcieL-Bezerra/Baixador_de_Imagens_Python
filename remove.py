import requests
url = 'https://roughs.ru/api/remove-bg'
files={'file': open('1.png', 'rb')}

response = requests.post(
    url,files=files   
)
if response.status_code == requests.codes.ok:
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)