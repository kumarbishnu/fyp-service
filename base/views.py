from rest_framework.decorators import api_view
from rest_framework.response import Response
from .courses import courses
from .models import *
from .serializers import *


# Create your views here.
@api_view(['GET'])
def get_routes(request):
    routes = [
        '/api/courses/',
        '/api/courses/create/',
        '/api/courses/:id/',
    ]
    return Response(routes)


@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_courses(request):
    return Response(courses)


@api_view(['GET'])
def get_course(request, pk):
    course = filter(lambda x: x['id'] == pk, courses)
    return Response(course)
