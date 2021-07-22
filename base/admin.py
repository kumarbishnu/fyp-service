from django.contrib import admin
from .models import *
from .users.models import *
from .courses.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Chapter)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Lecture)
admin.site.register(Profile)
admin.site.register(Resource)
