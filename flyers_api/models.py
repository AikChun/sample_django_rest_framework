from django.db import models

# Create your models here.
class Flyer(models.Model):
    street = models.CharField(max_length=50)
    city   = models.CharField(max_length=50)
    state  = models.CharField(max_length=50)

    class Meta:
        verbose_name        = "Flyer"
        verbose_name_plural = "Flyers"

    def __unicode__(self):
        return self.name

