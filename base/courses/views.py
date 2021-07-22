from .models import Course, Enrollment, Lecture
from .serializers import CourseSerializer, CourseSerializerWithContent
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
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
@permission_classes([IsAuthenticated])
def upload_course_image(request):
    data = request.data
    course = Course.objects.get(pk=data['course'])
    course.image = request.FILES.get('image')
    course.save()
    return Response('Image Uploaded')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_lecture_file(request):
    data = request.data
    lecture = Lecture.objects.get(pk=data['lecture'])
    lecture.file_content = request.FILES.get('file')
    lecture.save()
    return Response('File Uploaded')
