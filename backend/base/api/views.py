from rest_framework.response import Response
from rest_framework import generics

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from base.models import Batch, Note, Assay
from .serializers import AssaySerializer, BatchSerializer, NoteSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
      token = super().get_token(user)
      # Add custom claims
      token['username'] = user.username
      # ...
      return token

class MyTokenObtainPairView(TokenObtainPairView):
  serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
  routes = [
    '/api/token',
    '/api/token/refresh'
  ]
  return Response(routes)

class NoteListCreateAPIView(generics.ListCreateAPIView):
  queryset = Note.objects.all()
  serializer_class = NoteSerializer

note_list_create_view = NoteListCreateAPIView.as_view()

# @permission_classes([IsAuthenticated])
class BatchListAPIView(generics.ListCreateAPIView):
  queryset = Batch.objects.all()
  serializer_class = BatchSerializer

batch_list_view = BatchListAPIView.as_view()

class AssayListAPIView(generics.ListCreateAPIView):
  queryset = Assay.objects.all()
  serializer_class = AssaySerializer

assay_list_view = AssayListAPIView.as_view()


 






