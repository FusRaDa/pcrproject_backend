from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Note(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  body = models.TextField()

def validate_nonzero(value):
    if value == 0:
        raise ValidationError(
            _('Quantity %(value)s is not allowed'),
            params={'value': value},
        )

class Batch(models.Model):
  # firstAccessionNumber = models.CharField(max_length=25)
  # lastAccessionNumber = models.CharField(max_length=25)
  # client = models.CharField(max_length=25)

  assayCode = models.CharField(max_length=25)
  #assay name associated with assay code

  # numberOfSamples = models.PositiveSmallIntegerField(default=0, validators=[validate_nonzero])
  # #number of tests in assay code
  # #calculate number of tests = tests in assay code * number of samples

  # isBatchProccessed = models.BooleanField(default=False)

  batchDate = models.DateTimeField(auto_now_add=True)
  # # dueDate = batchDate + 48hours

  # TYPES = (
  #   ('dna', 'DNA'),
  #   ('rna', 'RNA'),
  #   ('dna&rna', 'DNA & RNA')
  # )

  # geneticType = models.CharField(choices=TYPES)


# class Assay(models.Model):
#   name = models.CharField(max_length=25)
#   code = models.CharField(max_length=25)






