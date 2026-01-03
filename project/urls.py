"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from recipes.views import home, contact, about


def hello_world(request):
    html = """<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <title>Hello</title>
  <style>
    :root {
      --bg-start: #3b0a5a;
      --bg-end: #0b6b42;
    }
    html, body {
      height: 100%;
      margin: 0;
    }
    body {
      display: flex;
      align-items: center;
      justify-content: center;
      background: linear-gradient(140deg, var(--bg-start) 0%, var(--bg-end) 100%);
      font-family: "Impact", "Franklin Gothic Heavy", "Haettenschweiler", sans-serif;
      font-size: 80px;
      font-weight: 900;
      letter-spacing: 1.5px;
      text-align: center;
    }
    .neon {
      background: linear-gradient(
        90deg,
        #ff0000,
        #ff7f00,
        #ffff00,
        #00ff00,
        #0000ff,
        #4b0082,
        #8b00ff,
        #ff0000
      );
      background-size: 700% 100%;
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
      text-shadow:
        0 0 8px rgba(255, 0, 140, 0.65),
        0 0 16px rgba(0, 255, 255, 0.5),
        0 0 28px rgba(255, 255, 0, 0.5);
      animation: rainbowWave 6s linear infinite;
    }
    @keyframes rainbowWave {
      0% { background-position: 0% 50%; }
      100% { background-position: 100% 50%; }
    }
  </style>
</head>
<body>
  <div class=\"neon\">hello world from Django</div>
</body>
</html>
"""
    return HttpResponse(html)

def my_view(request):
    ...
    return HttpResponse("This is my view!")


urlpatterns = [
    path("hello/", hello_world, name="hello_world"),
    path("", include("recipes.urls")),
]
