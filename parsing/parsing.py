import requests
from bs4 import BeautifulSoup


url = "https://avtokavkaza.ru/"

headers = {
    "Accept": "*/*",
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
}

req = requests.get(url)