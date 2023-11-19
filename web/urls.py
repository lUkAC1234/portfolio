from django.urls import path,include
from .views import index, ProjectsView

app_name = "main"

urlpatterns = [
    path('', index.as_view(), name="index"),
    path('projects', ProjectsView.as_view(), name="projects"),
]
