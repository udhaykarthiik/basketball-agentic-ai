from django.urls import path
from . import views

urlpatterns = [
    path("analyze/", views.analyze_logs, name="analyze_logs"),
]
