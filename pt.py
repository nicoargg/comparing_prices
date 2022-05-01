import requests
from lxml import etree

url = 'https://listado.mercadolibre.com.ar/mouse#D[A:mouse,L:undefined]'
req = requests.get(url, auth=('user', 'pass'))

req = req.text
tree = etree.HTML(req)

expression = '//span[@class="price-tag ui-search-price__part"]//span[@class="price-tag-fraction"]/text()'
print(tree.xpath(expression))



#content = req.content

#print(content)