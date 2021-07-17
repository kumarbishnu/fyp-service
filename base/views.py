from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def get_routes(request):
    routes = [
        '/api/courses/',
        '/api/courses/create/',
        '/api/courses/:id/',
    ]
    return Response(routes)
