from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
import socket

def health_check(request):
    return HttpResponse("OK", status=200)

def hostname_view(request):
    return HttpResponse(f"Hostname: {socket.gethostname()}")

def index(request):
    return HttpResponse("""
    <h1>Django Kubernetes App</h1>
    <p>Hostname: <strong>{}</strong></p>
    <p><a href="/health/">Health Check</a></p>
    <p><a href="/hostname/">Hostname</a></p>
    """.format(socket.gethostname()))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check),
    path('hostname/', hostname_view),
    path('', index),
]