from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    gender = models.CharField(max_length=6, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='user_profiles')

    def __str__(self):
        return self.user.first_name


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


class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.student.username + ' - ' + self.course.title


class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    number = models.IntegerField()
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Lecture(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    number = models.IntegerField()
    title = models.CharField(max_length=256)
    text_content = models.TextField(null=True, blank=True)
    file_content = models.FileField(null=True, blank=True, upload_to='lecture_files')

    def __str__(self):
        return self.title


class Resource(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=256, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.display_name
