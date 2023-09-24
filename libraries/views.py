from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Materi
from django.conf import settings
import os


# Create your views here.
@login_required
def index(request):
    if request.method == "GET":
        posts = Materi.objects.all().order_by("-tanggal").order_by("-waktu")
        search = request.GET.get("search")
        if search != None:
            posts = Materi.objects.filter(judul__icontains=search)

        context = {"posts": posts}
        return render(request, "libraries/index.html", context=context)
    return render(request, "libraries/index.html", context=context)


@login_required
def upload(request):
    if request.method == "POST":
        judul = request.POST["judul"]

        files = request.FILES.getlist("files")
        nama_file = ""
        for file in files:
            nama_file += file.name + " | "
        nama_file = nama_file[:-3]

        new_materi = Materi(user=request.user, judul=judul, nama_file=nama_file)
        new_materi.save()

        dir = os.path.join(
            settings.MEDIA_ROOT,
            str(new_materi.tanggal) + "/",
        )

        if not os.path.exists(dir):
            os.makedirs(dir)

        for file in files:
            file_path = os.path.join(dir, file.name)
            with open(file_path, "wb+") as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

        return render(request, "libraries/upload.html", {"msg": "berhasil upload"})
    return render(request, "libraries/upload.html")


from django.http import FileResponse


@login_required
def download(request, id, nama_file):
    post = Materi.objects.get(id=id)

    file_path = os.path.join(
        settings.MEDIA_ROOT,
        str(post.tanggal) + "/" + nama_file,
    )

    # # Open the file and create a FileResponse object
    file_response = FileResponse(open(file_path, "rb"))

    # # Set the appropriate content type and content-disposition headers
    file_response["Content-Type"] = "application/octet-stream"
    file_response["Content-Disposition"] = f'attachment; filename="{nama_file}"'

    return file_response


def delete(request, id):
    post = Materi.objects.get(id=id)
    post.delete()
    return redirect("my_post")


@login_required
def my_post(request):
    post = Materi.objects.filter(user=request.user)
    print(post)
    return render(request, "libraries/my_post.html", context={"data": post})


@login_required
def detail(request, id):
    post = Materi.objects.get(id=id)
    print(post.judul)
    nama_file = post.nama_file.split(" | ")
    context = {"post": post, "nama_file": nama_file}
    return render(request, "libraries/detail.html", context=context)
