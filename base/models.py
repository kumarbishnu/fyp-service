from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    tutor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    level = models.CharField(max_length=16)
    image = models.ImageField(null=True, blank=True, upload_to='course_thumbnails')
    # price =
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2)
    review_count = models.IntegerField(null=True, blank=True, default=0)
    lecture_count = models.IntegerField(null=True, blank=True, default=0)
    student_count = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.title
