import xml.etree.ElementTree as ET

# Creando el XML
zoo = ET.Element('zoo')
mamiferos = ET.SubElement(zoo, 'mamiferos')
reptiles = ET.SubElement(zoo, 'reptiles')
aves = ET.SubElement(zoo, 'aves')
# ------------------------------------------
animal1 = ET.SubElement(mamiferos, 'animal').text = 'Elefante'
animal2 = ET.SubElement(mamiferos, 'animal').text = 'Lobo'
animal3 = ET.SubElement(reptiles, 'animal').text = 'Caiman'
animal4 = ET.SubElement(reptiles, 'animal').text = 'Tortuga'
animal5 = ET.SubElement(aves, 'animal').text = 'Aguila'
animal6 = ET.SubElement(aves, 'animal').text = 'Pato'
# ------------------------------------------

mydata = ET.tostring(zoo)
myfile = open('zoo.xml', 'wb')
myfile.write(mydata)
myfile.close()

# Leyendo el XML
tree = ET.parse('zoo.xml')
root = tree.getroot()
print('-'*40)
for elem in root:
    print('---', elem.tag.upper(), '---')

    for subelem in elem:
        print('\t', subelem.text)
print('-'*40)
