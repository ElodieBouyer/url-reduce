from rest_framework.parsers import JSONParser

from reduce.models import MinUrl
from reduce.serializers import MinUrlSerializer


def add(request):
    data = JSONParser().parse(request)
    serializer = MinUrlSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
