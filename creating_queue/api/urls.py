from api.views import processing_command
from django.urls import path

urlpatterns = [
    path('processing_command/', processing_command),
]
