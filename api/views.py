from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerializer

from base.models import MusicLibrary

@api_view(['GET'])
def getDummyData(request):
    dummy = {
        'title': 'Dummy Data',
        'artist': 'Dummy Singer',
        'length': 'Dummy Length',
    }

    return Response(dummy)

@api_view(['GET'])
def getMusicData(request):
    data = MusicLibrary.objects.filter().first()   # not meaningful variable name
    serializer = ItemSerializer(data, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def addMusicData(request):
    serializer = ItemSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)