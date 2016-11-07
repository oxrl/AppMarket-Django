from django.db import models

# Create your models here.
class Marks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
            return '{}'.format(self.name)
