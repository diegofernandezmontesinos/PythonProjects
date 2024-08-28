import bs4
import requests



'''

resultado = requests.get('https://escueladirecta-blog.blogspot.com/')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

#columna_lateral = sopa.select('.sidebar-blog')

images = sopa.select('img')

for i in images:
    print(i)
'''

url_base = 'http://books.toscrape.com/catalogue/category/books_{}/index.html'

titulos_rating_alto = []

for pagina in range(1,50):
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    libros = sopa.select('.product_pod')

    for libro in libros:
        if len(libro.select('.start-rating.Four')) !=0 or len(libro.select('.start-rating.Five')) != 0:
            titulo_libro = libro.select('a')[1]['title']
            print(titulo_libro)
            titulos_rating_alto.append(titulo_libro)


for t in titulos_rating_alto:
    print(t)
