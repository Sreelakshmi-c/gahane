from django.urls import path
from .import views
urlpatterns=[
    path('home',views.fnHome,name='home'),
    path('signin',views.fnSignin,name='signin'),
    path('signup',views.fnSignup,name='signup'),
   
]