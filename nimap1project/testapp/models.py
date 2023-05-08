from django.db import models

# Create your models here.
class User(models.Model):

    uno=models.IntegerField()
    uname=models.CharField(max_length=20)
    ucity=models.CharField(max_length=20)
    uproject = models.CharField(max_length=20)
    uassinged = models.CharField(max_length=20)


    def __str__(self):
        return self.uname



class Client(models.Model):

    cno=models.IntegerField()
    cname=models.CharField(max_length=20)
    ccity=models.CharField(max_length=20)

    def __str__(self):
        return self.cname
