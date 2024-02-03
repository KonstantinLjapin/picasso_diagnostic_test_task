from django.urls import path
from .views import FileUploadAPIView, FilesAPIView


urlpatterns = [
    path('upload/', FileUploadAPIView.as_view(), name='upload-file'),
    path('files/', FilesAPIView.as_view(), name='files'),
]
