from flask import Flask, request
from flask_cors import CORS
from xml.etree import ElementTree as ET
from xml.dom import minidom


class ListaTareas:
    def __init__(self):
        self.lista_tareas = []

    def add(self, tarea):
        self.lista_tareas.append(tarea)


class Tarea:
    def __init__(self, titulo, fecha, estado, desc):
        self.titulo = titulo
        self.fecha = fecha
        self.estado = estado
        self.desc = desc


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origin": "*"}})

lista_tareas = ListaTareas()


@app.route('/tareas', methods=['GET'])
def get_tareas():
    document = minidom.Document()
    root = document.createElement('tareas')

    for tarea in lista_tareas.lista_tareas:
        tarea_e = document.createElement('tarea')
        root.appendChild(tarea_e)

        titulo = document.createElement('titulo')
        titulo.appendChild(document.createTextNode(tarea.titulo))
        tarea_e.appendChild(titulo)

        fecha = document.createElement('fecha')
        fecha.appendChild(document.createTextNode(tarea.fecha))
        tarea_e.appendChild(fecha)

        # estado = document.createElement('estado')
        # estado.appendChild(document.createTextNode(tarea.estado))
        # tarea_e.appendChild(estado)

        # desc = document.createElement('desc')
        # desc.appendChild(document.createTextNode(tarea.desc))
        # tarea_e.appendChild(desc)

    xml_file = root.toprettyxml(indent='\t', encoding='utf-8')
    return xml_file


@app.route('/tareas', methods=['POST'])
def post_tareas():
    xml_str = request.data.decode('utf-8')
    root = ET.fromstring(xml_str)

    for child in root:
        titulo = child.find('titulo').text
        fecha = child.find('fecha').text
        estado = child.find('estado').text
        desc = child.find('desc').text

        lista_tareas.add(Tarea(titulo, fecha, estado, desc))

    return ''


@app.route('/por-fecha', methods=['GET'])
def get_por_fecha():
    fecha = request.args.get('fecha')
    contador = 0
    for tarea in lista_tareas.lista_tareas:
        if tarea.fecha == fecha:
            contador += 1
    return str(contador)


if __name__ == '__main__':
    app.run(debug=True)