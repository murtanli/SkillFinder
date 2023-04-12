from django.db import models
from django.urls import reverse

class users(models.Model):
    login = models.CharField(max_length=15)
    Password = models.CharField(max_length=10)

class profile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    surname = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    user = models.ForeignKey(users,on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

class worker(models.Model):
    profile_wor = models.ForeignKey(profile, on_delete=models.PROTECT, db_index=True)
    def get_absolute_url(self):
        return reverse('post', kwargs={'work_id': self.pk})

class customer(models.Model):
    profile_cus = models.ForeignKey(profile, on_delete=models.PROTECT, db_index=True)
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

class order(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    worker = models.ForeignKey(worker, on_delete=models.PROTECT)
    customer = models.ForeignKey(customer, on_delete=models.PROTECT)
