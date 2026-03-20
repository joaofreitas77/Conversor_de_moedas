from django.contrib import admin
from django.urls import path
from app.views import converter_view

urlpatterns = [
    path('converter/', converter_view),
]
