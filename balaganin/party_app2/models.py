from django.db import models
from django.utils import timezone
import django_filters


class Category(models.Model):

    name = models.CharField(max_length=100, blank=True)
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name


class EventList(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    event_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    link = models.URLField(max_length=200, default='www.google.com')
    venue = models.CharField(max_length=200, null=True)
    image = models.ImageField(blank=True, upload_to='party_pics')
    country_choices= (
        ('MEXICO','MEXICO'),
        ('ISRAEL','ISRAEL'),
        ('FRANCE','FRANCE'),
        ('SPAIN','SPAIN'),
        ('GERMANY','GERMANY'),
        ('ENGLAND','ENGLAND')
    )
    country = models.CharField(max_length=20,choices=country_choices, default='MEXICO')
    price_choices = (
        ('$','$'),
        ('$$','$$'),
        ('$$$','$$$'),
        ('$$$$','$$$$')
    )
    price = models.CharField(max_length=10, choices=price_choices, default='$$$')

    class Meta:
        ordering = ["event_date"]
    def __str__(self):
        return self.title





