from django.db import models


class User(models.Model):
    username = models.CharField(max_length=25)
    f_name = models.CharField(max_length=25)
    l_name = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    registrate_date = models.DateField(auto_now=True)
    full_name = ''

    @property
    def full_name(self):
        return self.f_name + ' ' + self.l_name

    def __str__(self):
        return self.full_name


class Note(models.Model):
    category = [
        (1, 'Росход'),
        (2, 'Доход'),
    ]
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    category = models.IntegerField(choices=category)
    reason = models.CharField(max_length=75)
    price = models.IntegerField()
    date_time = models.DateTimeField(auto_now=True)






