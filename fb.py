import os
import requests
from requests import get
from bs4 import BeautifulSoup

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

clear()
print("Facebook Unfriend")
token = input("Masukan Akses Token lu : ")
tahun = input("Tahun Terakhir Post : ")
res = requests.post("https://api.ekawijanarka.info/fb/unfriend/index.php",{'token':token,'tahun':tahun})
respon = BeautifulSoup(res.text, 'html.parser')
result = respon.find('p', attrs={'align':'center','class':'pertama'})
print('\033[93m'+result.text)
