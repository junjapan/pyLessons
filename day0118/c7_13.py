import requests
response=requests.get('https://junjapan.github.io/Hobby/')
text=response.text
print(text)
