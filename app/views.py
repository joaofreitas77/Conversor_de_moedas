from django.shortcuts import render
import requests

# Create your views here.
def obterTaxa(moeda_origem, moeda_destino):
    url = f""