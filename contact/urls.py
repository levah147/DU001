from django.urls import path
from . import views
from .views import user_list

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('contact_thankyou/', views.contact_thankyou, name='contact_thankyou'),
    path('users/', user_list, name='user_list'),
    path('comments/', views.comment_list, name='comment_list'),
    path('add/', views.comment_add, name='comment_add'),
]
