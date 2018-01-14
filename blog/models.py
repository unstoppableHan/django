from django.db import models
from django.utils import timezone

# Create your models here.

class CryptoModel(models.Model):
    
    shortName = models.CharField(
        max_length = 50
    )

    fullName = models.CharField(
        max_length = 50
    )

    homePage = models.CharField(
        max_length = 200
    )

    altorithm = models.CharField(
        max_length = 200,
        null = True
    )

    description = models.TextField(
        null = True
    )

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    Publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    
    def __str__(self):
        return self.title

    def recent_publication(self):
        return self.publication_date >= timezone.now().date()