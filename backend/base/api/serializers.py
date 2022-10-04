from rest_framework.serializers import ModelSerializer
from base.models import Note, Batch

class NoteSerializer(ModelSerializer):
  class Meta:
    model = Note
    fields = '__all__'

class BatchSerializer(ModelSerializer):
  class Meta:
    model = Batch
    fields = '__all__'