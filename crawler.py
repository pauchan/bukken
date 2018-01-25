from lxml import html, etree
import requests

new_apartments_by_line = 'http://suumo.jp/jj/bukken/ichiran/JJ010FJ001/?ar=030&bs=020&ta=13'

response = requests.get(new_apartments_by_line)
tree = html.fromstring(response.content)

items = tree.xpath('//div[@class="property_unit-content"]/text()')

#items = tree.xpath('property_unit-content')

print ('Test: ', items)
