from django.http import JsonResponse


def index(request):
    # message = 'Welcome to DevsPrime Rest API. Visit /api'
    message = {
        'API endpoints': '/api/v1',
        'swagger documentation': '/swagger',
        'redoc documentation': '/redoc'
    }
    return JsonResponse(message)
