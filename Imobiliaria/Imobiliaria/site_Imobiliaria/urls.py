from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path('properties/',views.properties, name="properties"),
    path('messageEnviar/',views.messageEnviar, name="messageEnviar"),
]