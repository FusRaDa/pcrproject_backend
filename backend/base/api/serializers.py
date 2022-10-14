from pyexpat import model
from rest_framework.serializers import ModelSerializer
from base.models import Batch, Assay, Reagent, Supply, Label

class ReagentSerializer(ModelSerializer):
  class Meta:
    model = Reagent
    fields = ['name', 'catalogNumber', 'quantity', 'units', 'pk']

class SupplySerializer(ModelSerializer):
  class Meta:
    model = Supply
    fields = ['name', 'catalogNumber', 'quantity', 'units', 'pk']

class AssaySerializer(ModelSerializer):
  # group = serializers.SlugRelatedField(
  #   queryset=Assay.objects.all(),
  #   many=True,
  #   slug_field='code'
  # )

  # reagent = serializers.SlugRelatedField(
  #   queryset=Reagent.objects.all(),
  #   many=True,
  #   slug_field='name'
  # )

  class Meta:
    model = Assay
    fields = ['name', 'code', 'pk'] # include group, reagent, and supply as required later on

class BatchSerializer(ModelSerializer):
  # assay = serializers.SlugRelatedField(
  #   queryset=Assay.objects.all(),
  #   slug_field='code'
  # )

  class Meta:
    model = Batch
    # fields = ['assay', 'numberOfSamples', 'miscFields', 'batchDate', 'pk']
    fields = ['fieldLabels', 'pk']

class LabelSerializer(ModelSerializer):
  class Meta:
    model = Label
    fields = ['label', 'pk']


