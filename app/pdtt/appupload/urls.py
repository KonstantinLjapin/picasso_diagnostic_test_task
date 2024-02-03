from django.urls import path
from .views import FileUploadAPIView


urlpatterns = [
    path('upload-file/', FileUploadAPIView.as_view(), name='upload-file'),
]
