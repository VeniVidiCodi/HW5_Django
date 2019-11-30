import requests
import json

from django.http import HttpResponse
from django.shortcuts import render



def index(request): 
    print('- - - - - -  accessing INDEX page')
    context = {
        "index": "active",
    }
    return render(request, "index.html", context)


def about(request):
    print('- - - - - -  accessing ABOUT page')
    context = {
        "about": "active",
    }
    return render(request, "about.html", context)


def projects(request): 
    print('- - - - - -  accessing PROJECTS page')
    response = requests.get('https://api.github.com/users/venividicodi/repos')
    github_repos = response.json()
    context = {
        "projects": "active",
        "github_repos": github_repos
    }
    return render(request, "projects.html", context)
