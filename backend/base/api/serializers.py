from wsgiref.validate import validator
from rest_framework.serializers import ModelSerializer
from base.models import Note, Batch, Assay
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class NoteSerializer(ModelSerializer):
  class Meta:
    model = Note
    fields = '__all__'

class AssaySerializer(ModelSerializer):
  group = serializers.SlugRelatedField(
    queryset=Assay.objects.all(),
    many=True,
    slug_field='code'
  )

  class Meta:
    model = Assay
    fields = ['name', 'code', 'group']

class BatchSerializer(ModelSerializer):
  assay = serializers.SlugRelatedField(
    queryset=Assay.objects.all(),
    slug_field='code'
  )

  class Meta:
    model = Batch
    fields = ['assay', 'numberOfSamples', 'isBatchProccessed', 'batchDate', 'miscFields', 'pk']


