from django.urls import path
from .views import Welcome, Login

urlpatterns = [
    path('', Welcome.as_view(), name='welcome'),
    path('login/', Login.as_view(), name='login'),
]
