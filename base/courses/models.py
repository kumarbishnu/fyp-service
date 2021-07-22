from django.db import models
from django.contrib.auth.models import User


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
