import requests
import re
from requests.compat import quote_plus
from django.shortcuts import render
from .models import Search
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    return render(request, 'base.html')