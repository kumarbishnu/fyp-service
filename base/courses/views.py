from .models import Category, Course, Enrollment, Lecture
from .serializers import CourseSerializer, CourseSerializerWithContent
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


@api_view(['GET'])
def get_courses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_course(request, pk):
    course = Course.objects.get(id=pk)
    serializer = CourseSerializer(course, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_course_content(request, pk):
    user = request.user
    course = Course.objects.get(pk=pk)
    if (user.is_staff and course.tutor == user) or (not user.is_staff and Enrollment.objects.get(course=course, student=user)):
        serializer = CourseSerializerWithContent(course, many=False)
        return Response(serializer.data)
    return Response('Invalid Data')


@api_view(['POST'])
@permission_classes([IsAdminUser])
def upload_course_image(request):
    data = request.data
    course = Course.objects.get(pk=data['course'])
    course.image = request.FILES.get('image')
    course.save()
    return Response('Image Uploaded')


@api_view(['POST'])
@permission_classes([IsAdminUser])
def upload_lecture_file(request):
    data = request.data
    lecture = Lecture.objects.get(pk=data['lecture'])
    lecture.file_content = request.FILES.get('file')
    lecture.save()
    return Response('File Uploaded')


@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_course(request):
    data = request.data
    user = request.user
    category = Category.objects.get(pk=data['category'])
    course = Course.objects.create(
        title=data['title'],
        description=data['description'],
        tutor=user,
        category=category,
        level=data['level']
    )
    serializer = CourseSerializer(course, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def update_course(request):
    data = request.data
    course = Course.objects.get(pk=data['id'])
    if course.tutor != request.user:
        return Response('You do not own this course!')
    category = Category.objects.get(pk=data['category'])
    course.title = data['title']
    course.description = data['description']
    course.category = category
    course.level = data['level']
    course.save()
    serializer = CourseSerializer(course, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def delete_course(request):
    data = request.data
    course = Course.objects.get(pk=data['id'])
    if course.tutor != request.user:
        return Response('You do not own this course!')
    course.delete()
    return Response('Course Deleted!')
