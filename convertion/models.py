from django.db import models

# Create your models here.
class data(models.Model):
    value=models.IntegerField()
    result=models.CharField(
        max_length=255,
        default="null",
    )
        

    2
