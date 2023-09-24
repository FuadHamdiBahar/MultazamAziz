from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("upload/", views.upload, name="upload"),
    path("mypost/", views.my_post, name="my_post"),
    path("detail/<id>", views.detail, name="detail"),
    path("download/<id>/<nama_file>", views.download, name="download"),
    path("delete/<id>", views.delete, name="hapus"),
]
