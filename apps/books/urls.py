from django.conf.urls import url
from . import views         # This line is new!

urlpatterns = [
    url(r'addBook', views.addBook),
    url(r'delete(?P<id>\d+)', views.delete),
    url(r'edit_book', views.edit_book),
    url(r'edit(?P<id>\d+)', views.edit),
    url(r'^', views.index),
]
