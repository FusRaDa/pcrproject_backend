from rest_framework.response import Response
from rest_framework import generics

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from base.models import Batch, Assay, Reagent
from .serializers import AssaySerializer, BatchSerializer, ReagentSerializer


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

#Reagent
class ReagentListCreateAPIView(generics.ListCreateAPIView):
  queryset = Reagent.objects.all()
  serializer_class = ReagentSerializer

reagent_list_create_view = ReagentListCreateAPIView.as_view()

class ReagentRetrieveUpdateDestroyAPIView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
  queryset = Reagent.objects.all()
  serializer_class = ReagentSerializer
  lookup_field = 'pk'

reagent_retrieve_update_destroy = ReagentRetrieveUpdateDestroyAPIView.as_view()
















#Assay
class AssayListAPIView(generics.ListCreateAPIView):
  queryset = Assay.objects.all()
  serializer_class = AssaySerializer

assay_list_view = AssayListAPIView.as_view()


class AssayCreateAPIView(generics.CreateAPIView):
  queryset = Assay.objects.all()
  serializer_class = AssaySerializer

assay_create_view = AssayCreateAPIView.as_view()

class AssayRetrieveAPIView(generics.RetrieveAPIView):
  queryset = Assay.objects.all()
  serializer_class = AssaySerializer
  lookup_field = 'pk'

assay_retrieve_view = AssayRetrieveAPIView.as_view()


class AssayUpdateAPIView(generics.UpdateAPIView):
  queryset = Assay.objects.all()
  serializer_class = AssaySerializer
  lookup_field = 'pk'

assay_update_view = AssayUpdateAPIView.as_view()


class AssayDestroyAPIView(generics.DestroyAPIView):
  queryset = Assay.objects.all()
  serializer_class = AssaySerializer
  lookup_field = 'pk'

assay_destroy_view = AssayDestroyAPIView.as_view()


#Batch
# @permission_classes([IsAuthenticated])
class BatchListAPIView(generics.ListAPIView):
  queryset = Batch.objects.all()
  serializer_class = BatchSerializer

batch_list_view = BatchListAPIView.as_view()


class BatchRetrieveAPIView(generics.RetrieveAPIView):
  queryset = Batch.objects.all()
  serializer_class = BatchSerializer
  lookup_field = 'pk'

batch_retrieve_view = BatchRetrieveAPIView.as_view()


class BatchCreateAPIView(generics.CreateAPIView):
  queryset = Batch.objects.all()
  serializer_class = BatchSerializer

batch_create_view = BatchCreateAPIView.as_view()


class BatchUpdateAPIView(generics.UpdateAPIView):
  queryset = Batch.objects.all()
  serializer_class = BatchSerializer
  lookup_field = 'pk'

batch_update_view = BatchUpdateAPIView.as_view()


class BatchDestroyAPIView(generics.DestroyAPIView):
  queryset = Batch.objects.all()
  serializer_class = BatchSerializer
  lookup_field = 'pk'

batch_destroy_view = BatchDestroyAPIView.as_view()







 






