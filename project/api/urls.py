from django.urls import path
from config.views import index
from api.views.register_view import RegisterView

urlpatterns = [
    path('', index),
    path('register/', RegisterView.as_view(), name='register'),
]
