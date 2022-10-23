from rest_framework.serializers import ModelSerializer
from base.models import Batch, Assay, Reagent, Supply, Label
from rest_framework import serializers

class ReagentSerializer(ModelSerializer):
  class Meta:
    model = Reagent
    fields = ['name', 'catalogNumber', 'quantity', 'units', 'pk']
    extra_kwargs = {
      'name' : {'validators': []},
      'catalogNumber' : {'validators': []},
    }

  def validate_name(self, value):
    check_query = Reagent.objects.filter(name=value)
    if check_query.exists() and not (
        isinstance(self.parent, BatchSerializer)
        and self.field_name == "assay"
    ):
        raise serializers.ValidationError(
            "Reagent with this name already exists!"
        )
    if not check_query.exists():
        raise serializers.ValidationError(
            "Reagent with this name was not found!"
        )
    return value

  def validate_catalogNumber(self, value):
    check_query = Reagent.objects.filter(catalogNumber=value)
    if check_query.exists() and not (
        isinstance(self.parent, BatchSerializer)
        and self.field_name == "assay"
    ):
        raise serializers.ValidationError(
            "Reagent with this catalog number already exists!"
        )
    if not check_query.exists():
        raise serializers.ValidationError(
            "Reagent with this catalog number was not found!"
        )
    return value
 


#not in use right now
class SupplySerializer(ModelSerializer):
  class Meta:
    model = Supply
    fields = ['name', 'catalogNumber', 'quantity', 'units', 'pk']



class GroupAssay(ModelSerializer):
  reagent = ReagentSerializer(many=True)
  class Meta:
    model = Assay
    fields = ['name', 'code', 'type', 'reagent', 'pk']

class AssaySerializer(ModelSerializer):
  group = GroupAssay(many=True)

  #frontend - only allow a reagent to be added if there is no group of assays
  reagent = ReagentSerializer(many=True)

  class Meta:
    model = Assay
    fields = ['name', 'code', 'type', 'reagent', 'group', 'pk'] # include group, reagent, and supply as required later on
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

  #exp
  # def create(self, validated_data):
  #   reagent_validated = validated_data.get('reagent')
  #   if reagent_validated:
  #     validated_data['reagent'] = Reagent.objects.get(
  #         name=reagent_validated.get('name'),
  #         catalogNumber=reagent_validated.get('catalogNumber'),
  #     )
  
  #   project = Reagent.objects.create(**validated_data)
  #   return project


  #ensures that assay can either have zero or more than one assay in group
  # def clean(self):
  #   group = self.cleaned_data.get('group')
  #   if group and group.count() == 1:
  #     raise serializers.ValidationError('Assay must either have no assays or more than one in its group')
  #   return self.cleaned_data

class BatchSerializer(ModelSerializer):
  assay = AssaySerializer(required=True)
  
  class Meta:
    model = Batch
    fields = ['assay', 'numberOfSamples', 'isBatchProcessed', 'batchDate', 'fieldLabels', 'pk']
  
  #create
  def create(self, validated_data):
    assay_validated = validated_data.get('assay')
    if assay_validated:
      validated_data["assay"] = Assay.objects.get(
          code=assay_validated.get('code'),
          name=assay_validated.get('name'),
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


