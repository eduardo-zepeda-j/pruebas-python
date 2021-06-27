from django.shortcuts import render,redirect
import requests
# Create your views here.

endpoint='http://localhost:5000{}'

def index(request):
    if request.method=='GET':
        url = endpoint.format('/datos')#concatena en las llaves el string asignado a format
        data = requests.get(url)
        context ={
            'data':data.text,
        }

        return render(request,'index.html',context)

    elif request.method =='POST':
        docs = request.FILES['document']
        data = docs.read()
        url = endpoint.format('/datos')
        requests.post(url,data)
        return redirect('index')

def reports(request):
    if request.method =='GET':
        date = request.GET.get('date',None)
        code = request.GET.get('code',None)

        context = {
            'date':None,
            'code':None,
        }
        if date !=None:
            context['data']=date
        if code != None:
            context['code'] = code
        return render(request,'reports.html',context)

def calc(request):
    if request.method == 'GET':
        num_1 = request.GET.get('num_1', 0)
        num_2 = request.GET.get('num_2', 0)

        url = endpoint.format('/potencia')

        potencia = requests.get(url, {
            'num_1': num_1,
            'num_2': num_2,
        })

        context = {
            'potencia': potencia.text,
        }

        return render(request, 'calc.html', context)