from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    is_tutor = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'is_tutor']

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email
        return name

    def get_is_tutor(self, obj):
        return obj.is_staff


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'is_tutor', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class ProfileSerializer(UserSerializer):
    phone = serializers.CharField(source='profile.phone')
    address = serializers.CharField(source='profile.address')
    gender = serializers.CharField(source='profile.gender')
    dob = serializers.CharField(source='profile.dob')
    image = serializers.CharField(source='profile.image.url')

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'is_tutor',
                  'phone', 'address', 'gender', 'dob', 'image']


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
