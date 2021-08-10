from django.shortcuts import render, redirect
import requests as req
import re

# Create your views here.


def index(request):
    xml_data = req.get('http://localhost:5000/tareas')
    xml_str = xml_data.text
    context = {'dato': xml_str}
    return render(request, 'index.html', context)


def reportes(request):
    if request.method == 'GET':
        fecha = request.GET.get('fecha', None)

        contador_fecha = req.get('http://localhost:5000/por-fecha', {
            'fecha': fecha
        }).text

        context = {'fecha': contador_fecha}

    return render(request, 'reportes.html', context)


def recibir_xml(request):
    if request.method == 'POST':
        xml_file = request.FILES['docs']
        xml_data = xml_file.read()

    req.post('http://localhost:5000/tareas', xml_data)
    return redirect('index')
