from requests import get 
from bs4 import BeautifulSoup

base_url = "https://books.toscrape.com/"
response = get(base_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')
    print(f"Tamanho do HTML: {len(response.text)} caracteres")

    book = soup.findAll(class_= 'product_pod')
    print(f"Número de livros encontrados: {len(book)}")


else:
    print(f"❌ Erro: {response.status_code}")

