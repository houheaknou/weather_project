from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        # db_table = ''
        # managed = True
        # verbose_name = 'ModelName'
        verbose_name_plural = 'cities'