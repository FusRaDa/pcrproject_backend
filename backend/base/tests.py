from django.test import TestCase
from base.models import Batch



class ExtractionGroupTest(TestCase):


  def test_batch(self, value):
    check_query = Batch.objects.filter(dna_extraction=value)
    print(check_query)
   
 


   