from django.db import models

# Create your models here.
class medicine(models.Model):
    name=models.CharField(max_length=50)
    company=models.CharField(max_length=50)
    expiry_date=models.DateField(max_length=50)

    def __str__(self) :
        return self.name