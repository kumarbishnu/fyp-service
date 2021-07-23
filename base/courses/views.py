from .models import Category, Chapter, Course, Enrollment, Lecture, Resource
from .serializers import ChapterSerializer, CourseSerializer, CourseSerializerWithContent, LectureSerializer, ResourceSerializer
from django.core.exceptions import ObjectDoesNotExist
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
    if user.is_staff:
        if course.tutor == user:
            serializer = CourseSerializerWithContent(course, many=False)
        else:
            return Response('You do not own this course.')
    else:
        try:
            Enrollment.objects.get(course=course, student=user)
            serializer = CourseSerializerWithContent(course, many=False)
        except ObjectDoesNotExist:
            return Response('You do not own this course.')
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def upload_course_image(request):
    data = request.data
    course = Course.objects.get(pk=data['course'])
    course.image = request.FILES.get('image')
    course.save()
    return Response(course.image.url)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def upload_lecture_file(request):
    data = request.data
    lecture = Lecture.objects.get(pk=data['lecture'])
    lecture.file_content = request.FILES.get('file')
    lecture.save()
    return Response(lecture.file_content.url)


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


@api_view(['PUT'])
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


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_course(request, pk):
    course = Course.objects.get(pk=pk)
    if course.tutor != request.user:
        return Response('You do not own this course!')
    course.delete()
    return Response('Course Deleted!')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_chapter(request):
    data = request.data
    chapter = Chapter.objects.create(
        course=Course.objects.get(pk=data['course']),
        number=data['number'],
        title=data['title'],
    )
    serializer = ChapterSerializer(chapter, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_chapter(request):
    data = request.data
    chapter = Chapter.objects.get(pk=data['id'])
    chapter.number = data['number']
    chapter.title = data['title']
    chapter.save()
    serializer = ChapterSerializer(chapter, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_chapter(request, pk):
    chapter = Chapter.objects.get(pk=pk)
    chapter.delete()
    return Response('Chapter Deleted!')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_lecture(request):
    data = request.data
    lecture = Lecture.objects.create(
        course=Chapter.objects.get(pk=data['chapter']),
        number=data['number'],
        title=data['title'],
        text_content=data['text_content'],
    )
    serializer = LectureSerializer(lecture, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_lecture(request):
    data = request.data
    lecture = Lecture.objects.get(pk=data['id'])
    lecture.number = data['number']
    lecture.title = data['title']
    lecture.text_content = data['text_content']
    lecture.save()
    serializer = LectureSerializer(lecture, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_lecture(request, pk):
    lecture = Lecture.objects.get(pk=pk)
    lecture.delete()
    return Response('Lecture Deleted!')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_resource(request):
    data = request.data
    resource = Resource.objects.create(
        course=Lecture.objects.get(pk=data['lecture']),
        display_name=data['display_name'],
        url=data['url'],
    )
    serializer = ResourceSerializer(resource, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_resource(request):
    data = request.data
    resource = Resource.objects.get(pk=data['id'])
    resource.display_name = data['display_name']
    resource.url = data['url']
    resource.save()
    serializer = ResourceSerializer(resource, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_resource(request, pk):
    resource = Resource.objects.get(pk=pk)
    resource.delete()
    return Response('Resource Deleted!')
