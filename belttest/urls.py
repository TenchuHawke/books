from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.main.urls', namespace='main')),
    url(r'^login', include('apps.login.urls', namespace='login')),
    url(r'^books', include('apps.books.urls', namespace='books')),
    url(r'^main', include('apps.main.urls')),
]
