from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Materi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    judul = models.CharField(max_length=255)
    nama_file = models.CharField(max_length=1000)
    tanggal = models.DateField(auto_now_add=True)
    waktu = models.TimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.id, self.judul)