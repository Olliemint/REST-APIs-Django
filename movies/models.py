from django.db import models

# Create your models here.
class Moviedata(models.Model):
    
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    ratings = models.FloatField()
    movietype = models.CharField(max_length=200,default='action')
    
    def __str__(self):
        
        return self.name
        
        