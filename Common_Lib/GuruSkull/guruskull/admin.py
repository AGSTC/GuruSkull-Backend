from django.contrib import admin
from .models import *  # imports all models from models.py

# Dynamically register all models in the app
from django.apps import apps

app = apps.get_app_config('guruskull')
for model_name, model in app.models.items():
    admin.site.register(model)
