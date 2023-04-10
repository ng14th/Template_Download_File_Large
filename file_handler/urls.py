from django.urls import path
from . import views
from .views import FileView


app_name = 'store'

urlpatterns = [
    path("files/", FileView.as_view(), name="files"),
    #path("files/<int:pk>", FileDetailView.as_view(), name="files-detail"),
]