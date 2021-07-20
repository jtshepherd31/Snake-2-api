from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.highscore import Highscore
from ..serializers import HighscoreSerializer

# Create your views here.
class Highscores(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = HighscoreSerializer
    def get(self, request):
        """Index request"""
        highscores = Highscore.objects.filter(owner=request.user.id)
        data = HighscoreSerializer(highscores, many=True).data
        return Response({ 'highscores': data })

    def post(self, request):
        """Create request"""
        request.data['highscore']['owner'] = request.user.id
        highscore = HighscoreSerializer(data=request.data['highscore'])
        if highscore.is_valid():
            highscore.save()
            return Response({ 'highscore': highscore.data }, status=status.HTTP_201_CREATED)
        return Response(highscore.errors, status=status.HTTP_400_BAD_REQUEST)

class HighscoreDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        highscore = get_object_or_404(Highscore, pk=pk)
        data = HighscoreSerializer(highscore).data
        return Response({ 'highscore': data })

    def delete(self, request, pk):
        """Delete request"""
        highscore = get_object_or_404(Highscore, pk=pk)
        if not request.user.id == highscore.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this highscore')
        highscore.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        highscore = get_object_or_404(Highscore, pk=pk)
        if not request.user.id == highscore.owner.id:
            raise PermissionDenied('Unauthorized, you do not own this highscore')

        request.data['highscore']['owner'] = request.user.id
        data = HighscoreSerializer(highscore, data=request.data['highscore'], partial=True)
        if data.is_valid():
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
