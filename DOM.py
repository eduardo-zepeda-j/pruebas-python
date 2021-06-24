from xml.dom import minidom

mydoc = minidom.parse('d:Desktop/python/clase5.xml')
items = mydoc.getElementsByTagName('item')
# print(items[1].firstChild.data)
# print(items)
# print(items[0].attributes['name'].value)

for element in items:
    print(element.firstChild.data)
 #   print(element.attributes['name'].value)

#print('Cantidad de elementos:',len(items))
