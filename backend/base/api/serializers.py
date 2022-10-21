from dataclasses import field
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

class GroupAssay(ModelSerializer):
  class Meta:
    model = Assay
    fields = '__all__'

class AssaySerializer(ModelSerializer):
  group = GroupAssay(many=True)

  # reagent = serializers.SlugRelatedField(
  #   queryset=Reagent.objects.all(),
  #   many=True,
  #   slug_field='name'
  # )

  class Meta:
    model = Assay
    fields = ['name', 'code', 'group', 'pk'] # include group, reagent, and supply as required later on
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

  #ensures that assay can either have zero or more than one assay in group
  def clean(self):
    group = self.cleaned_data.get('group')
    if group and group.count() == 1:
      raise serializers.ValidationError('Assay must either have no assays or more than one in its group')
    return self.cleaned_data

class BatchSerializer(ModelSerializer):
  assay = AssaySerializer(required=True)
  
  class Meta:
    model = Batch
    fields = ['assay', 'numberOfSamples', 'isBatchProcessed', 'batchDate', 'fieldLabels', 'pk']
  
  #create
  def create(self, validated_data):
    assay_validated = validated_data.get("assay")
    if assay_validated:
      validated_data["assay"] = Assay.objects.get(
          code=assay_validated.get("code"),
          name=assay_validated.get("name")
      )
    project = Batch.objects.create(**validated_data)
    return project

  def update(self, instance, validated_data):
    assay_validated = validated_data.get("assay")

    instance.assay = Assay.objects.get(
        name=assay_validated.get('name'),
        code=assay_validated.get("code")
      )

    instance.numberOfSamples = validated_data.get('numberOfSamples', instance.numberOfSamples)
    instance.isBatchProcessed = validated_data.get('isBatchProcessed', instance.isBatchProcessed)
    instance.batchDate = validated_data.get('batchDate', instance.batchDate)
    instance.fieldLabels = validated_data.get('fieldLabels', instance.fieldLabels)
    instance.save()

    return instance
    
    
   

   

   

 











     
    


class LabelSerializer(ModelSerializer):
  class Meta:
    model = Label
    fields = ['label', 'pk']


