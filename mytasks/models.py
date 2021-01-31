from django.db import models


class Mesagesender(models.Model):
    name = models.CharField(max_length=64, unique=True)
    img = models.ImageField(upload_to='mesagesender', blank=True, null=True)

    def __str__(self):
        return self.name


class Tasksender(models.Model):
    name = models.EmailField(max_length=50, unique=True)
    family = models.ForeignKey(Mesagesender, on_delete=models.PROTECT, db_index=True)

    unique_together = [['name', 'family']]

    def __str__(self):
        return self.name
