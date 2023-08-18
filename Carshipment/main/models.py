from django.db import models

# Create your models here.
class Car(models.Model):
    manufacturer = models.TextField()
    seria = models.TextField()
    model = models.TextField()
    year = models.IntegerField()
    mileage = models.IntegerField()

    class Meta:
        db_table = 'Cars'

    def __str__(self):
        return f"{self.model} ({self.year})"
    

class News(models.Model):
    title = models.TextField()
    text = models.TextField()
    img_address = models.TextField()
    place = models.TextField()
    date = models.DateField()

    class Meta:
        db_table = 'News'

    def __str__(self):
        return self.title