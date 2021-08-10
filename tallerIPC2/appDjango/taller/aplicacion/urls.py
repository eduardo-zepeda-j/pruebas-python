
from django.urls import path
from aplicacion import views

urlpatterns = [

    path('',views.index, name = 'home')
]
