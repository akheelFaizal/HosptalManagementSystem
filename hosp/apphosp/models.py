from django.db import models


# Create your models here.

class newmember(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    status_choices = [('male', 'male'), ('female', 'female'), ('not specified', 'not specified')]
    gender = models.CharField(max_length=25, choices=status_choices, default='not specified')

    def __str__(self):
        return self.name


class appointments(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    status_choices = [('male', 'male'), ('female', 'female'), ('not specified', 'not specified')]
    gender = models.CharField(max_length=25, choices=status_choices, default='not specified')
    phone_number = models.CharField(max_length=200)
    additional_comments = models.CharField(max_length=400)
    payment = models.CharField(max_length=200, default=0)
    booking_status = [
        ('approve', 'approve'),
        ('reject', 'reject'),
        ('pending', 'pending')
    ]
    bk_status = models.CharField(max_length=25, choices=booking_status, default='pending')

    def __str__(self):
        return self.name


class admin_log(models.Model):
    adName = models.CharField(max_length=200)
    adPass = models.CharField(max_length=200)

    def __str__(self):
        return self.adName


class doctorAdd(models.Model):
    name = models.CharField(max_length=200)
    docId = models.CharField(max_length=200)
    photoDoc = models.FileField(max_length=200)
    department = models.CharField(max_length=200)

    def __str__(self):
        return self.name
