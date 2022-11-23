from rest_framework.serializers import ModelSerializer
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
  reagent = ReagentSerializer(many=True, read_only=True)
  supply = SupplySerializer(many=True, read_only=True) 

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
  assay = GroupAssaySerializer(many=True, read_only=True)
  reagent = ReagentSerializer(many=True, read_only=True)
  supply = SupplySerializer(many=True, read_only=True)

  #frontend - only allow a reagent to be added if there is no group of assays
  reagent_ids = serializers.PrimaryKeyRelatedField(queryset=Reagent.objects.all(), many=True, required=False, write_only=True)
  supply_ids = serializers.PrimaryKeyRelatedField(queryset=Supply.objects.all(), many=True, required=False, write_only=True)
  assay_ids = serializers.PrimaryKeyRelatedField(queryset=Assay.objects.all(), many=True, required=False, write_only=True)

  class Meta:
    model = Assay
    fields = ['name', 'code', 'type', 'reagent', 'supply', 'assay', 'pk', 'reagent_ids', 'supply_ids', 'assay_ids'] # include group, reagent, and supply as required later on
    extra_kwargs = {
      'name' : {'validators': []},
      'code' : {'validators': []},
    }

  def validate_code(self, value):
    check_query = Assay.objects.filter(code=value)
    if self.context['request']._request.method == 'POST':
      if check_query.exists() and not (
        isinstance(self.parent, BatchSerializer)
        and self.field_name == "assay"):
        raise serializers.ValidationError("Assay with this code already exists.")

      if not check_query.exists() and not (isinstance(self, AssaySerializer)):
        raise serializers.ValidationError("Assay with this code was not found.")

    if self.context['request']._request.method == 'PUT' and not (isinstance(self.parent, BatchSerializer)):
      if self.instance.code != value and check_query.exists():
          raise serializers.ValidationError("Assay with this code already exists")
    return value

  def validate_name(self, value):
    check_query = Assay.objects.filter(name=value)
    if self.context['request']._request.method == 'POST':
      if check_query.exists() and not (
        isinstance(self.parent, BatchSerializer)
        and self.field_name == "assay"):
        raise serializers.ValidationError("Assay with this name already exists.")

      if not check_query.exists() and not (isinstance(self, AssaySerializer)):
        raise serializers.ValidationError("Assay with this name was not found.")

    if self.context['request']._request.method == 'PUT' and not (isinstance(self.parent, BatchSerializer)):
        if self.instance.name != value and check_query.exists():
          raise serializers.ValidationError("Assay with this name already exists")
    return value

  def create(self, validated_data):
    reagent_ids = validated_data.pop('reagent_ids', [])
    supply_ids = validated_data.pop('supply_ids', [])
    assay_ids = validated_data.pop('assay_ids', [])

    if len(assay_ids) == 1:
      raise serializers.ValidationError(
        "Grouped assays cannot contain only one assay"
      )
    
    # if len(assay_ids) == 0 and (len(reagent_ids) == 0 or len(supply_ids) == 0):
    #   raise serializers.ValidationError(
    #     "Individual assays must have reagents and supplies"
    #   )
    
    if len(assay_ids) > 0 and (len(reagent_ids) > 0 or len(supply_ids) > 0):
      raise serializers.ValidationError(
        "Grouped assay cannot contain reagents and supplies"
      )

    instance = Assay.objects.create(**validated_data)
    
    for reagent in reagent_ids:
      instance.reagent.add(reagent)

    for supply in supply_ids:
      instance.supply.add(supply)

    for assay in assay_ids:
      instance.assay.add(assay)

    return instance


  def update(self, instance, validated_data):
    reagent_ids = validated_data.pop('reagent_ids', [])
    supply_ids = validated_data.pop('supply_ids', [])
    assay_ids = validated_data.pop('assay_ids', [])

    if len(assay_ids) == 1:
      raise serializers.ValidationError(
        "Grouped assays cannot contain only one assay"
      )
    
    # if len(assay_ids) == 0 and (len(reagent_ids) == 0 or len(supply_ids) == 0):
    #   raise serializers.ValidationError(
    #     "Individual assays must have reagents and supplies"
    #   )

    
    if len(assay_ids) > 0 and (len(reagent_ids) > 0 or len(supply_ids) > 0):
      raise serializers.ValidationError(
        "Grouped assay cannot contain reagents and supplies"
      )

    instance.name = validated_data.get('name', instance.name)
    instance.code = validated_data.get('code', instance.code)
    instance.type = validated_data.get('type', instance.type)

    instance.save()

    assays = Assay.objects.get(pk=instance.pk)

    if len(reagent_ids) > 0:
      assays.reagent.clear()
      for reagent in reagent_ids:
        assays.reagent.add(reagent)

    if len(supply_ids) > 0:
      assays.supply.clear()
      for supply in supply_ids:
        assays.supply.add(supply)

    if len(assay_ids) > 0:
      assays.assay.clear()
      for assay in assay_ids:
        assays.assay.add(assay)
  
    return instance


class BatchSerializer(ModelSerializer):
  # two errors concerning extraction groups:
  # 1-an extraction group is unique for either dna or rna/total-nucleic
  # 2-updating an extraction group from dna to rna (vice verse) is not allowed, MUST delete and create a new batch
  # OR disable updating assay in batch
  assay = AssaySerializer(required=True)
  batchDate = serializers.DateTimeField(required=False, format="%Y-%m-%d %H:%M")
  
  class Meta:
    model = Batch
    fields = ['assay', 'numberOfSamples', 'isBatchProcessed', 'batchDate', 'dna_extraction', 'rna_extraction', 'fieldLabels', 'pk']
    extra_kwargs = {
      'dna_extraction' : {'validators': []},
      'rna_extraction' : {'validators': []},
    }


  def validate_dna_extraction(self, value):
    if len(value) != 3 or value.isalpha() is False or value.isupper() is False:
      raise serializers.ValidationError(
        "Extraction group must be a three capitalized letter field."
      )
    if value is not None:
      check_query_dna = Batch.objects.filter(dna_extraction=value)
      check_query_rna = Batch.objects.filter(rna_extraction=value)
      if check_query_rna.exists():
        raise serializers.ValidationError(
          "Batch with this extraction group already exists."
      )
      if check_query_dna.exists():
        raise serializers.ValidationError(
          "Batch with this extraction group already exists."
      )
    return value


  def validate_rna_extraction(self, value):
    if len(value) != 3 or value.isalpha() is False or value.isupper() is False:
      raise serializers.ValidationError(
        "Extraction group must be a three capitalized letter field."
      )
    if value is not None:
      check_query_dna = Batch.objects.filter(dna_extraction=value)
      check_query_rna = Batch.objects.filter(rna_extraction=value)
      if check_query_dna.exists():
        raise serializers.ValidationError(
          "Batch with this extraction group already exists."
        )
      if check_query_rna.exists():
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
          "Batch cannot share the same extraction groups."
      )
    instance = Batch.objects.create(**validated_data)
    return instance


  #reagent issue - custom update
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
   
    instance.fieldLabels = validated_data.get('fieldLabels', instance.fieldLabels)
    instance.save()

    return instance
    
    
class LabelSerializer(ModelSerializer):
  class Meta:
    model = Label
    fields = ['label', 'pk']
    # extra_kwargs = {
    #   'label' : {'validators': []},
    # }


