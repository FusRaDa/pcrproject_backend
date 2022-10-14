from rest_framework.response import Response
from rest_framework import generics

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from base.models import Batch, Assay, Reagent, Supply, Label
from .serializers import AssaySerializer, BatchSerializer, LabelSerializer, ReagentSerializer, SupplySerializer


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
class ReagentListAPIView(generics.ListAPIView):
  queryset = Reagent.objects.all()
  serializer_class = ReagentSerializer

reagent_list_view = ReagentListAPIView.as_view()


class ReagentCreateAPIView(generics.CreateAPIView):
  queryset = Reagent.objects.all()
  serializer_class = ReagentSerializer

reagent_create_view = ReagentCreateAPIView.as_view()


class ReagentRetrieveAPIView(generics.RetrieveAPIView):
  queryset = Reagent.objects.all()
  serializer_class = ReagentSerializer
  lookup_field = 'pk'

reagent_retrieve_view = ReagentRetrieveAPIView.as_view()


class ReagentUpdateAPIView(generics.UpdateAPIView):
  queryset = Reagent.objects.all()
  serializer_class = ReagentSerializer
  lookup_field = 'pk'

reagent_update_view = ReagentUpdateAPIView.as_view()

class ReagentDestroyAPIView(generics.DestroyAPIView):
  queryset = Reagent.objects.all()
  serializer_class = ReagentSerializer
  lookup_field = 'pk'

reagent_destroy_view = ReagentDestroyAPIView.as_view()


#Supply
class SupplyListAPIView(generics.ListAPIView):
  queryset = Supply.objects.all()
  serializer_class = SupplySerializer

supply_list_view = SupplyListAPIView.as_view()


class SupplyCreateAPIView(generics.CreateAPIView):
  queryset = Supply.objects.all()
  serializer_class = SupplySerializer

supply_create_view = SupplyCreateAPIView.as_view()


class SupplyRetrieveAPIView(generics.RetrieveAPIView):
  queryset = Supply.objects.all()
  serializer_class = SupplySerializer
  lookup_field = 'pk'

supply_retrieve_view = SupplyRetrieveAPIView.as_view()


class SupplyUpdateAPIView(generics.UpdateAPIView):
  queryset = Supply.objects.all()
  serializer_class = SupplySerializer
  lookup_field = 'pk'

supply_update_view = SupplyUpdateAPIView.as_view()


class SupplyDestroyAPIView(generics.DestroyAPIView):
  queryset = Supply.objects.all()
  serializer_class = SupplySerializer
  lookup_field = 'pk'

supply_destroy_view = SupplyDestroyAPIView.as_view()


#Assay
class AssayListAPIView(generics.ListAPIView):
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
@permission_classes([IsAuthenticated])
class BatchListAPIView(generics.ListAPIView):
  queryset = Batch.objects.all()
  serializer_class = BatchSerializer

batch_list_view = BatchListAPIView.as_view()


@permission_classes([IsAuthenticated])
class BatchRetrieveAPIView(generics.RetrieveAPIView):
  queryset = Batch.objects.all()
  serializer_class = BatchSerializer
  lookup_field = 'pk'

batch_retrieve_view = BatchRetrieveAPIView.as_view()


@permission_classes([IsAuthenticated])
class BatchUpdateAPIView(generics.UpdateAPIView):
  queryset = Batch.objects.all()
  serializer_class = BatchSerializer
  lookup_field = 'pk'

batch_update_view = BatchUpdateAPIView.as_view()


@permission_classes([IsAuthenticated])
class BatchDestroyAPIView(generics.DestroyAPIView):
  queryset = Batch.objects.all()
  serializer_class = BatchSerializer
  lookup_field = 'pk'

batch_destroy_view = BatchDestroyAPIView.as_view()


@permission_classes([IsAuthenticated])
class BatchCreateAPIView(generics.CreateAPIView):
  queryset = Batch.objects.all()
  serializer_class = BatchSerializer

batch_create_view = BatchCreateAPIView.as_view()




#labels - for column names in master sheet
@permission_classes([IsAuthenticated])
class LabelListAPIView(generics.ListAPIView):
  queryset = Label.objects.all()
  serializer_class = LabelSerializer

label_list_view = LabelListAPIView.as_view()


@permission_classes([IsAuthenticated])
class LabelRetrieveAPIView(generics.RetrieveAPIView):
  queryset = Label.objects.all()
  serializer_class = LabelSerializer
  lookup_field = 'pk'

label_retrieve_view = LabelRetrieveAPIView.as_view()


@permission_classes([IsAuthenticated])
class LabelUpdateAPIView(generics.UpdateAPIView):
  queryset = Label.objects.all()
  serializer_class = LabelSerializer
  lookup_field = 'pk'

label_update_view = LabelUpdateAPIView.as_view()


@permission_classes([IsAuthenticated])
class LabelDestroyAPIView(generics.DestroyAPIView):
  queryset = Label.objects.all()
  serializer_class = LabelSerializer
  lookup_field = 'pk'

label_destroy_view = LabelDestroyAPIView.as_view()


@permission_classes([IsAuthenticated])
class LabelCreateAPIView(generics.CreateAPIView):
  queryset = Label.objects.all()
  serializer_class = LabelSerializer

label_create_view = LabelCreateAPIView.as_view()









 






