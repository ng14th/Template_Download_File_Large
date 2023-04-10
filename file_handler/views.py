from rest_framework import status, generics
from rest_framework.response import Response
from .models import FileTemplate
from .serializers import FileSerializer



class FileView(generics.ListCreateAPIView):
    serializer_class = FileSerializer

    def get_queryset(self):
        return FileTemplate.objects.all()

    def create(self, request, *args, **kwargs):
        file_serializer = self.get_serializer(data=self.request.data)

        if not file_serializer.is_valid():
            return Response(
                {"message": "Created File unsuccessfully!", "success": False},
                status=status.HTTP_400_BAD_REQUEST,
            )
        file_serializer.save()
        
        return Response(
            data={"message": "Created File successfully!", "success": True},
            status=status.HTTP_201_CREATED,
        )