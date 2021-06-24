import xml.etree.ElementTree as ET
#----------------leer documentos
"""

print(root[1][0].attrib)

tree = ET.parse('d:Desktop/python/clase5.xml')
root = tree.getroot()

for elem in root:
    for subelem in elem.findall('item'):
        print(subelem.attrib)
        print(subelem.get('name'))

#modificar un elemento 
#changing a field text
for element in root.iter('item'):
    element.text='Clase0806'
"""



#--------------- escribir documentos
#data = ET.Element('data')
#items = ET.SubElement(data,'items')
#SubElement(parent,tag,attrib={},**extra)

zoo = ET.Element('zoo')
mamiferos =ET.SubElement(zoo,'mamiferos')
mamiferos.set('nombre','animal1')
mamiferos.text = 'Leon'

mydata = ET.tostring(zoo)
myfile = open('zoo.xml','wb')
myfile.write(mydata)

