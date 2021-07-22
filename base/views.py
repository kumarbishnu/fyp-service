from base.courses.models import Category
from base.courses.serializers import CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def get_routes(request):
    routes = [
        '/api/categories/',
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
