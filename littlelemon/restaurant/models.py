from django.db import models

# Create your models here.
class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10,decimal_places=1)
    Inventory = models.CharField(max_length=5)

    #add the following method in Menu class
    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'

class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()

