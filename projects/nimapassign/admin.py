# project_management/admin.py
from django.contrib import admin 
from nimapassign.models import Client 
from nimapassign.models import User
from nimapassign.models import Project
admin.site.register(Client)
admin.site.register(User)
admin.site.register(Project)