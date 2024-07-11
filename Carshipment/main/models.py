from django.db import models

# Create your models here.
class Car(models.Model):
    manufacturer = models.TextField()
    model = models.TextField()
    generation = models.TextField() 
    year = models.IntegerField()
    mileage = models.IntegerField()
    color = models.TextField()
    engine_type = models.TextField()
    engine_capacity = models.DecimalField(max_digits=5, decimal_places=2)
    engine_cylinder = models.TextField()
    engine_power_hp = models.IntegerField() 
    engine_power_kw = models.IntegerField()
    transmission = models.TextField()
    drive = models.TextField()
    acceleration_0_100 = models.DecimalField(max_digits=5, decimal_places=2)
    max_speed = models.IntegerField()
    price = models.TextField()
    img_addresses = models.TextField()
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


class Request(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.TextField()
    name = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.TextField()
    comment = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        db_table = 'Requests'

    def __str__(self):
        return f"Заявка {self.id} от {self.date} {self.time}: {self.subject} - {self.name}"