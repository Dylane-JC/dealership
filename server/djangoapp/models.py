from django.db import models
from django.utils.timezone import now

# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    ids = models.AutoField(primary_key=True)
# - Name
    name = models.CharField(max_length=25)
# - Description
    description = models.CharField(max_length=25)
# - Any other fields you would like to include in car make model
    year = models.DateField(max_length=6)
    color = models.CharField(max_length=25)
# - __str__ method to print a car make object
    def __str__(self):
        return self.name

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
class CarModel(models.Model):
    ids = models.AutoField(primary_key=True)
# - Name
    name = models.CharField(max_length=25)
# Foreign key
    carmake = models.ForeignKey(CarMake, on_delete=models.CASCADE)
# - Dealer id, used to refer a dealer created in cloudant database
    id_dealer = models.IntegerField()
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
    list_choice = [
        (1, ('Sedan')), 
        (2, ('SUV')), 
        (3, ('WAGON'))
        ]
    types = models.CharField(max_length=30, null=True)
# - Year (DateField)
    year = models.DateField()
# - Any other fields you would like to include in car model
    seler = models.CharField(max_length=25)
# - __str__ method to print a car make object
    def __str__(self):
        return self.name


# <HINT> Create a plain Python class `CarDealer` to hold dealer data

class CarDealer:
    def __init__(self, address, city, full_name, ids, lat, longs, short_name, st, zips)
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.ids = ids
        # Location lat
        self.lat = lat
        # Location long
        self.longs = longs
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zips = zips
    def __str__(self):
        return "Dealer name : " + self.full_name
        
# <HINT> Create a plain Python class `DealerReview` to hold review data
if __name__ == "__main__":
    pass
