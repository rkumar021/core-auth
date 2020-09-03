from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Role(models.Model):
    STUDENT = 1
    TEACHER = 2
    ADMIN = 3
    ROLE_CHOICES = (
      (STUDENT, 'student'),
      (TEACHER, 'teacher'),
      (ADMIN, 'admin'),
  )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class User(AbstractUser):
    roles = models.ManyToManyField(Role)