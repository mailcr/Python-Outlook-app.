from django.conf.urls import url
from django.urls import path
from tutorial import views

app_name = 'tutorial'

urlpatterns = [
	path('',views.home,name='home'),
	path('home/',views.home, name='home'),
	path('gettoken/',views.gettoken, name='gettoken'),
    path('mail/',views.mail,name='mail'),
    path('events/', views.events, name='events'),
    path('contacts/',views.contacts, name='contacts'),
]