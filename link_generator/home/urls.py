from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('link', views.NewLinkView.as_view(), name='link'),
    path('about', views.about, name='about')
]
