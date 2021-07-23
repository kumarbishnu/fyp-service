from base.users.serializers import UserSerializer
from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TutorSerializer(UserSerializer):
    image = serializers.CharField(source='profile.image.url')

    class Meta:
        model = User
        fields = ['name', 'image']


class CourseSerializer(serializers.ModelSerializer):
    category_id = serializers.CharField(source='category.id')
    category = serializers.CharField(source='category.name')
    tutor = TutorSerializer(many=False)

    class Meta:
        model = Course
        fields = '__all__'


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'


class LectureSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(source='resource_set', read_only=True, many=True)

    class Meta:
        model = Lecture
        fields = '__all__'


class ChapterSerializer(serializers.ModelSerializer):
    lectures = LectureSerializer(source='lecture_set', read_only=True, many=True)

    class Meta:
        model = Chapter
        fields = '__all__'


class CourseSerializerWithContent(CourseSerializer):
    chapters = ChapterSerializer(source='chapter_set', read_only=True, many=True)

    class Meta:
        model = Course
        fields = '__all__'
