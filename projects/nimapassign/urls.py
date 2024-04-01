

from django.urls import path
from .views import client_detail, client_list, create_project, project_list,project_detail

urlpatterns = [
    path('clients/', client_list),
    path('projects/', project_list),
    path('projects/<int:pk>/',project_detail),
    path('clients/<int:pk>/',client_detail),
    path('createproject/',create_project)
]
