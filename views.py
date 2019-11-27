import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request): 
    print('- - - - - -  accessing INDEX page')
    content_html = open("templates/index.html").read()
    # navbar = open("templates/navbar.html").read()
    # print(navbar)
    context = {
        "content": content_html,
        "title": "Home",
        # "navbar": navbar,
    }
    return render(request, "base.html", context)


def about(request):
    print('- - - - - -  accessing ABOUT page')
    content_html = open("templates/about.html").read()
    context = {
        "content": content_html,
        "title": "About",
    }
    return render(request, "base.html", context)


def projects(request): 
    print('- - - - - -  accessing PROJECTS page')
    # We can also combine Django with APIs
    # response = requests.get('https://api.github.dcom/users/michaelpb/repos')
    # repos = response.json()
    content_html = open("templates/projects.html").read()
    context = {
        "projects": content_html,
        "title": "Projects",
    }
    return render(request, "base.html", context)

