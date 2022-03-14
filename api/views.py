from json import JSONDecodeError
from django.http import JsonResponse

# Create your views here.

def home(request):
    return JsonResponse({'Info':'test api if works'})