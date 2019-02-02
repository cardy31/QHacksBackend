from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Scheduler(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=500)
    priority = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)],default=1)
    lengthOfTime = models.IntegerField(validators=[MinValueValidator(0)])
    category = models.CharField(max_length=200, blank=True, default='')
    description = models.CharField(max_length=1000, blank=True, default='')

    class Meta:
        ordering = ('priority',)



