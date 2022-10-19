from rest_framework.serializers import ModelSerializer
from base.models import Batch, Assay, Reagent, Supply, Label
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
    extra_kwargs = {
      'name' : {'validators': []},
      'code' : {'validators': []},
    }

  def validate_code(self, value):
    check_query = Assay.objects.filter(code=value)
    if check_query.exists() and not (
        isinstance(self.parent, BatchSerializer)
        and self.field_name == "assay"
    ):
        raise serializers.ValidationError(
            "Assay with this code already exists."
        )
    if not check_query.exists():
        raise serializers.ValidationError(
            "Assay with this code was not found."
        )
    return value

  def validate_name(self, value):
    check_query = Assay.objects.filter(name=value)
    if check_query.exists() and not (
        isinstance(self.parent, BatchSerializer)
        and self.field_name == "assay"
    ):
        raise serializers.ValidationError(
            "Assay with this name already exists."
        )
    if not check_query.exists():
        raise serializers.ValidationError(
            "Assay with this name was not found."
        )
    return value
   
class BatchSerializer(ModelSerializer):
  assay = AssaySerializer(required=True)
  
  class Meta:
    model = Batch
    fields = ['assay', 'numberOfSamples', 'isBatchProcessed', 'batchDate', 'fieldLabels', 'pk']

  def create(self, validated_data):
    assay_validated = validated_data.get("assay")
    if assay_validated:
        validated_data["assay"] = Assay.objects.get(
            code=assay_validated.get("code")
        )
    project = Batch.objects.create(**validated_data)
    return project

  def create(self, validated_data):
    assay_validated = validated_data.get("assay")
    if assay_validated:
        validated_data["assay"] = Assay.objects.get(
            name=assay_validated.get("name")
        )
    project = Batch.objects.create(**validated_data)
    return project


class LabelSerializer(ModelSerializer):
  class Meta:
    model = Label
    fields = ['label', 'pk']


