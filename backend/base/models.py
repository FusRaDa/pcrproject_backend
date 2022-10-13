from datetime import datetime
from email.policy import default
from random import choices
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.
def validate_nonzero(value):
    if value == 0:
        raise ValidationError(
            _('Quantity %(value)s is not allowed'),
            params={'value': value},
        )

def validate_quantity(value):
    if value <= 0:
        raise ValidationError(
            _('Quantity %(value)s is not allowed'),
            params={'value': value},
        )

LITERS = 'Liters'
MILLILITERS = 'Milliliters'
MICROLITERS = 'Microliters'
GRAMS = 'Grams'
MILLIGRAMS = 'Milligrams'

UNITS = [
  (LITERS, 'L'),
  (MILLILITERS, 'mL'),
  (MICROLITERS, '\u00B5L'),
  (GRAMS, 'g'),
  (MILLIGRAMS, 'mg')
]

class Reagent(models.Model):
  name = models.CharField(max_length=25, null=True, unique=True)
  catalogNumber = models.CharField(max_length=25, null=True, unique=True)
  quantity = models.DecimalField(max_digits=7, decimal_places=2, validators=[validate_quantity])
  units = models.CharField(max_length=15, choices=UNITS, default=LITERS)
  #additional fields: urls to reagent/supply to help track inventory

  def __str__(self):
    return self.name

class Supply(models.Model):
  name = models.CharField(max_length=25, null=True, unique=True)
  catalogNumber = models.CharField(max_length=25, null=True, unique=True)
  quantity = models.DecimalField(max_digits=7, decimal_places=2, validators=[validate_quantity])
  units = models.CharField(max_length=15, choices=UNITS, default=LITERS)
  #additional fields: urls to reagent/supply to help track inventory

  def __str__(self):
    return self.name

# not being used
def get_default_reagents():
  return {'reagents': []}

class Assay(models.Model):
  name = models.CharField(max_length=25, null=True, unique=True)
  code = models.CharField(max_length=25, null=True, unique=True)
  group = models.ManyToManyField('self', blank=True, default='null', symmetrical=False)
  #if assay contains a group do not include in group list - fix in frontend

  #make reagent and supply neccessary eventually...
  reagent = models.ManyToManyField(Reagent, blank=True)
  supply = models.ManyToManyField(Supply, blank=True)

  def __str__(self):
    return f'{self.code}-{self.name}'

# not being used
def get_default_miscFields():
  return {'miscFields': []}

#add Batch name later...
class Batch(models.Model):
  assay = models.ForeignKey(Assay, null=True, on_delete=models.SET_NULL)

  numberOfSamples = models.PositiveSmallIntegerField(default=0, validators=[validate_nonzero])
  #number of tests in assay code
  #calculate number of tests = tests in assay code * number of samples

  isBatchProccessed = models.BooleanField(default=False)

  batchDate = models.DateTimeField(default=datetime.now)
  # # dueDate = batchDate + 48hours

  miscFields = models.JSONField(blank=True, null=True, default=dict)
  # geneticType
  # firstAccessionNumber
  # lastAccessionNumber
  # client
  # group id's










