from .serializers import ProfileSerializer, UserSerializerWithToken
from base.courses.models import Course
from base.courses.serializers import CourseSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for key, value in serializer.items():
            data[key] = value
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def register_user(request):
    data = request.data
    is_tutor = False
    if data['role'] == 'Tutor':
        is_tutor = True
    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password']),
            is_staff=is_tutor
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists!'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    user = request.user
    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    data = request.data

    user = request.user
    profile = user.profile

    user.first_name = data['name']
    profile.phone = data['phone']
    profile.address = data['address']
    profile.gender = data['gender']
    profile.dob = data['dob']

    user.save()
    profile.save()

    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_courses(request):
    user = request.user
    if user.is_staff:
        courses = user.course_set.all()
    else:
        courses = Course.objects.filter(enrollment__student_id=user.id)
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)
