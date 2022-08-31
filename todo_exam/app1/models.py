from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Student(models.Model):
    ism = models.CharField(max_length=40)
    yosh = models.PositiveIntegerField()
    kurs = models.PositiveIntegerField()
    id_raqam = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism

class Todo(models.Model):
    CHOICE = (
        ["Bajarildi", "Bajarildi"],
        ["Bajarilmadi", "Bajarilmadi"],

    )
    title = models.CharField(max_length=40)
    sana = models.DateTimeField()
    description = models.TextField()
    status = models.CharField(choices=CHOICE, max_length=20)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


