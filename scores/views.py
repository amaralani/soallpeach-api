from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from scores.models import Score
from scores.serializers import ScoreSerializer


class ScoreView(APIView):
    def get(self, request):
        return Response(ScoreSerializer(instance=Score.objects.all(), many=True).data)

    def post(self, request):
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
