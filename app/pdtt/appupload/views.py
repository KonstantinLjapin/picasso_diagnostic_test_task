from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FileSerializer
from .models import File


class FileUploadAPIView(APIView):
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class FilesAPIView(APIView):
    serializer_class = FileSerializer

    def get(self, request, *args, **kwargs):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        if serializer.data:
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.data,
            status=status.HTTP_204_NO_CONTENT
        )
