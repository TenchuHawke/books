from django.conf.urls import url
from . import views

urlpatterns = [
   # This line has changed!
    url(r'^$', views.index, name = 'login_main'),
    url(r'/login', views.log_in, name = 'log_in'),
    url(r'register', views.register, name = 'register'),
    url(r'success', views.success, name='success'),
    url(r'logout', views.logout, name='logout'),
    url(r'^', views.index, name = 'login_main'),

]
