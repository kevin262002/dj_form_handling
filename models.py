from django.db import models

class Member(models.Model):
  first_name = models.CharField(max_length=25)
  last_name = models.IntegerField(max_length=5)
  roll_number = models.CharField(max_length=25)
  password = models.CharField(max_length=25)
  


