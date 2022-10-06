from datetime import datetime
from enum import unique
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Note(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  body = models.TextField()

class Assay(models.Model):
  name = models.CharField(max_length=25, null=True, unique=True)
  code = models.CharField(max_length=25, null=True, unique=True)
  group = models.ManyToManyField('self', blank=True, default='null')
  #if assay contains a group do not include in group list
  def __str__(self):
    return f'{self.code}-{self.name}'


def validate_nonzero(value):
    if value == 0:
        raise ValidationError(
            _('Quantity %(value)s is not allowed'),
            params={'value': value},
        )

class Batch(models.Model):
  assay = models.ForeignKey(Assay, null=True, on_delete=models.SET_NULL)

  # assayCode = GenericForeignKey(singleAssay, groupAssay)
  #assay name associated with assay code

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










