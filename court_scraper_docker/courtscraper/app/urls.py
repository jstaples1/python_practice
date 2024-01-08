from django.urls import path
from . import views


app_name = "app"

urlpatterns = [
  path('court/', views.court_view, name='court')
]