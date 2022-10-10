from wsgiref.validate import validator
from rest_framework.serializers import ModelSerializer
from base.models import Batch, Assay, Reagent, Supply
from rest_framework import serializers

class ReagentSerializer(ModelSerializer):
  class Meta:
    model = Reagent
    fields = ['name', 'catalogNumber', 'quantity', 'units', 'pk']

class SupplySerializer(ModelSerializer):
  class Meta:
    model = Supply
    fields = ['name', 'catalogNumber', 'quantity', 'units', 'pk']

class AssaySerializer(ModelSerializer):
  group = serializers.SlugRelatedField(
    queryset=Assay.objects.all(),
    many=True,
    slug_field='code'
  )

  class Meta:
    model = Assay
    fields = ['name', 'code', 'group', 'reagent', 'pk']

class BatchSerializer(ModelSerializer):
  assay = serializers.SlugRelatedField(
    queryset=Assay.objects.all(),
    slug_field='code'
  )

  class Meta:
    model = Batch
    fields = ['assay', 'numberOfSamples', 'miscFields', 'batchDate', 'pk']


