from django.urls import path
from .views import index, contato, produto,cliente

urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produto/<int:pk>', produto, name='produto'),
    path('cliente/<int:pk>', cliente, name='cliente'),
]