from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from base.models import Batch, Assay, Reagent, Supply, Label
from rest_framework import serializers

class ReagentSerializer(ModelSerializer):
  class Meta:
    model = Reagent
    fields = ['name', 'catalogNumber', 'quantity', 'units', 'pk']
  

#not in use right now
class SupplySerializer(ModelSerializer):
  class Meta:
    model = Supply
    fields = ['name', 'catalogNumber', 'quantity', 'units', 'pk']


class GroupAssay(ModelSerializer):
  reagent = ReagentSerializer(many=True)
  supply = SupplySerializer(many=True)

  class Meta:
    model = Assay
    fields = ['name', 'code', 'type', 'reagent', 'supply', 'pk']
    extra_kwargs = {
      'name' : {'validators': []},
      'code' : {'validators': []},
    }

  def validate_code(self, value):
    check_query = Assay.objects.filter(code=value)
    if not check_query.exists():
      raise serializers.ValidationError(
          "Assay with this code was not found."
      )
    if check_query.exists() and (isinstance(self.parent, BatchSerializer)):
      return value
    # elif check_query.exists() and (isinstance(self.parent, AssaySerializer)):
    #   raise serializers.ValidationError(
    #         "Assay with this code already exists."
    #     )

  def validate_name(self, value):
    check_query = Assay.objects.filter(name=value)
    if not check_query.exists():
      raise serializers.ValidationError(
          "Assay with this name was not found."
      )
    if check_query.exists() and (isinstance(self.parent, BatchSerializer)):
      return value


class AssaySerializer(ModelSerializer):
  group = GroupAssay(many=True)

  #frontend - only allow a reagent to be added if there is no group of assays
  reagent = ReagentSerializer(many=True)
  supply = SupplySerializer(many=True)

  class Meta:
    model = Assay
    fields = ['name', 'code', 'type', 'reagent', 'supply', 'group', 'pk'] # include group, reagent, and supply as required later on
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

  # ensures that when making an assay only either zero or more than one assay can be in the group
  # override create method?
  # def clean(self):
  #   group = self.cleaned_data.get('group')
  #   if group and group.count() == 1:
  #     raise serializers.ValidationError('Assay must either have no assays or more than one in its group')
  #   return self.cleaned_data



class BatchSerializer(ModelSerializer):
  assay = AssaySerializer(required=True)
  
  class Meta:
    model = Batch
    fields = ['assay', 'numberOfSamples', 'isBatchProcessed', 'batchDate', 'dna_extraction', 'rna_extraction', 'fieldLabels', 'pk']
    extra_kwargs = {
      'dna_extraction' : {'validators': []},
      'rna_extraction' : {'validators': []},
    }

  def validate_dna_extraction(self, value):
    check_query = Batch.objects.filter(rna_extraction=value)
    if check_query.exists():
      raise serializers.ValidationError(
          "Batch with this extraction group already exists."
      )
    return value

  def validate_rna_extraction(self, value):
    check_query = Batch.objects.filter(dna_extraction=value)
    if check_query.exists():
      raise serializers.ValidationError(
          "Batch with this extraction group already exists."
      )
    return value


  #create
  def create(self, validated_data):
    rna_validated = validated_data.get('rna_extraction')
    dna_validated = validated_data.get('dna_extraction')
    assay_validated = validated_data.get('assay')
    if assay_validated and rna_validated != dna_validated:
      validated_data["assay"] = Assay.objects.get(
          code=assay_validated.get('code'),
          name=assay_validated.get('name'),
      )
    else:
      raise serializers.ValidationError(
          "Batch with this extraction group already exists."
      )
    project = Batch.objects.create(**validated_data)
    return project


  #reagent issue - custome update
  def update(self, instance, validated_data):
    assay_validated = validated_data.get("assay")

    instance.assay = Assay.objects.get(
        name=assay_validated.get('name'),
        code=assay_validated.get('code'),
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


