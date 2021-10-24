from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('primeiro', views.primeiro, name='primeiro'),
    path('segundo', views.segundo, name='segundo'),
    path('terceiro', views.terceiro, name='terceiro')
]