import requests
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    print('------ accessing index page')
    # This is similar to ones we have done before. Instead of keeping
    # the HTML / template in a separate directory, we just reply with
    # the HTML embedded here.
    return HttpResponse('''
        <h1>Welcome to my home page!</h1>
        <a href="/about-me">About me</a> <br />
        <a href="/github-api-example">See my GitHub contributions</a> <br />
    ''')


def about_me(request):
    print('------ accessing about-me page')
    # Django comes with a "shortcut" function called "render", that
    # lets us read in HTML template files in separate directories to
    # keep our code better organized.
    context = {
        'name': 'Ash Ketchum',
        'pokemon': 'Pikachu',
    }
    return render(request, 'about_me.html', context)


def projects(request):
    print('------ accessing projects page')
    # We can also combine Django with APIs
    response = requests.get('https://api.github.com/users/michaelpb/repos')
    repos = response.json()
    context = {
        'projects': repos,
    }
    return render(request, 'projects.html', context)




def about(request):
    content_html = open("content/about.html").read()
    context = {
    "about": about_html,
    }
    return render(request, "base.html", context)

