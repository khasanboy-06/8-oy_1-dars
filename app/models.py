from django.db import models


class CarsInfo(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    content = models.TextField()


    def __str__(self):
        return self.name
    
    