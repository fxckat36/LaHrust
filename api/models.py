from django.db import models

class menu(models.Model):
    name = models.CharField(max_length = 80)
    cost = models.IntegerField()
    about = models.TextField()
    pic = models.FileField()

class feedback(models.Model):
    name = models.CharField(max_length= 30)
    comment = models.TextField()
    rate = models.IntegerField()
    # date = models.DateField()

    def __str__(self):
        return self.name
