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


class GroupAssaySerializer(ModelSerializer):
  reagent = ReagentSerializer(many=True, allow_null=True)
  supply = SupplySerializer(many=True, allow_null=True) 

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
    if check_query.exists() and (isinstance(self.parent, AssaySerializer)):
      return value

  def validate_name(self, value):
    check_query = Assay.objects.filter(name=value)
    if not check_query.exists():
      raise serializers.ValidationError(
          "Assay with this name was not found."
      )
    if check_query.exists() and (isinstance(self.parent, AssaySerializer)):
      return value


class AssaySerializer(ModelSerializer):
  assays = GroupAssaySerializer(many=True)

  #frontend - only allow a reagent to be added if there is no group of assays
  reagent = ReagentSerializer(many=True, allow_null=True)
  supply = SupplySerializer(many=True, allow_null=True)

  class Meta:
    model = Assay
    fields = ['name', 'code', 'type', 'reagent', 'supply', 'assays', 'pk'] # include group, reagent, and supply as required later on
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
    if not check_query.exists() and not isinstance(self, AssaySerializer):
      raise serializers.ValidationError(
          "Assay with this code was not found."
      )
    return value

  def validate_name(self, value):
    check_query = Assay.objects.filter(name=value)
    # throws error if query does not exist 
    # and request is not from BatchSerializer 
    # and requesting field name is not "assay"
    if check_query.exists() and not (
        isinstance(self.parent, BatchSerializer)
        and self.field_name == "assay"
    ):
      raise serializers.ValidationError(
          "Assay with this name already exists."
      )
    # throws error if query does not exist 
    # and request is not from AssaySerializer 
    if not check_query.exists() and not isinstance(self, AssaySerializer):
      raise serializers.ValidationError(
          "Assay with this name was not found."
      )
    return value


  def create(self, validated_data):
    reagent_data = validated_data.pop('reagent')
    supply_data = validated_data.pop('supply')
    assays_data = validated_data.pop('assays')

    if len(assays_data) == 1:
      raise serializers.ValidationError(
          "Grouped assay cannot contain only one assay"
      )
    
    if (len(assays_data) == 0) and ((len(reagent_data) == 0) or (len(supply_data) == 0)):
      raise serializers.ValidationError(
          "Individual assays must have reagents and supplies"
      )
    
    if (len(assays_data) > 1) and ((len(reagent_data) > 0) or (len(supply_data) > 0)):
      raise serializers.ValidationError(
          "Grouped assays cannot contain reagents and supplies"
      )

    all_data = Assay.objects.create(**validated_data)

    #make reagent neccessary in frontend for individual assays
    if reagent_data is not None:
      for reagent in reagent_data:
        d=dict(reagent)
        Reagent.objects.create(name=all_data, reagent=d['reagent'])

    #make supply neccessary in frontend for individual assays
    if supply_data is not None:
      for supply in supply_data:
        d=dict(supply)
        Supply.objects.create(name=all_data, supply=d['supply'])

    #make assays neccessary in frontend for group assays
    if assays_data is not None:
      for assay in assays_data:
        d=dict(assay)
        Assay.objects.create(name=all_data, assay=d['assays'])

    return all_data


  def update(self, instance, validated_data):
    reagent_data = validated_data.pop('reagent')
    supply_data = validated_data.pop('supply')
    assays_data = validated_data.pop('assays')

    if len(assays_data) == 1:
      raise serializers.ValidationError(
          "Grouped assay cannot contain only one assay"
      )
    
    if (len(assays_data) == 0) and ((len(reagent_data) == 0) or (len(supply_data) == 0)):
      raise serializers.ValidationError(
          "Individual assays must have reagents and supplies"
      )
    
    if (len(assays_data) > 1) and ((len(reagent_data) > 0) or (len(supply_data) > 0)):
      raise serializers.ValidationError(
          "Grouped assays cannot contain reagents and supplies"
      )

    for item in validated_data:
      if Assay._meta.get_field(item):
        setattr(instance, item, validated_data[item])
    Reagent.objects.filter(name=instance).delete()
    for reagent in reagent_data:
      d=dict(reagent)
      Reagent.objects.create(name=instance, reagent=d['reagent'])

    for item in validated_data:
      if Assay._meta.get_field(item):
        setattr(instance, item, validated_data[item])
    Supply.objects.filter(name=instance).delete()
    for supply in supply_data:
      d=dict(supply)
      Supply.objects.create(name=instance, supply=d['supply'])

    for item in validated_data:
      if Assay._meta.get_field(item):
        setattr(instance, item, validated_data[item])
    Assay.objects.filter(name=instance).delete()
    for assay in assays_data:
      d=dict(assay)
      Assay.objects.create(name=instance, assay=d['assays'])

    instance.save()
    return instance




class BatchSerializer(ModelSerializer):
  # two errors concerning extraction groups:
  # 1-an extraction group is unique for either dna or rna/total-nucleic
  # 2-updating an extraction group from dna to rna (vice verse) is not allowed, MUST delete and create a new batch
  # OR disable updating assay in batch
  assay = AssaySerializer(required=True)
  
  class Meta:
    model = Batch
    fields = ['assay', 'numberOfSamples', 'isBatchProcessed', 'batchDate', 'dna_extraction', 'rna_extraction', 'fieldLabels', 'pk']
    extra_kwargs = {
      'dna_extraction' : {'validators': []},
      'rna_extraction' : {'validators': []},
    }

  def validate_dna_extraction(self, value):
    if value is not None:
      check_query = Batch.objects.filter(rna_extraction=value)
      if check_query.exists():
        raise serializers.ValidationError(
            "Batch with this extraction group already exists."
      )
    return value

  def validate_rna_extraction(self, value):
    if value is not None:
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
          "Batch cannot share the same extraction groups"
      )
    instance = Batch.objects.create(**validated_data)
    return instance


  #reagent issue - custome update
  def update(self, instance, validated_data):
    assay_validated = validated_data.get("assay")

    instance.assay = Assay.objects.get(
        name=assay_validated.get('name'),
        code=assay_validated.get('code'),
      )

    instance.dna_extraction = validated_data.get('dna_extraction', instance.dna_extraction)
    instance.rna_extraction = validated_data.get('rna_extraction', instance.rna_extraction)

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


