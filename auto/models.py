from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Make(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name
    

class Auto(models.Model):
    name = models.CharField(max_length=200)
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(verbose_name="Price", validators=[MinValueValidator(1000, "The price can not be less than a thousand dollars!"), MaxValueValidator(100000000, "The price can not exceed 10 Millions dollars!")])
    mpg = models.PositiveIntegerField(verbose_name="Mileage (mpg)")
    rep78 = models.PositiveIntegerField(verbose_name="Repair record 1978", null=True)
    headroom = models.FloatField(verbose_name="Headroom (in.)")
    trunk = models.PositiveIntegerField(verbose_name="Trunk (in.)")
    weight = models.PositiveIntegerField(verbose_name="Weight (lbs.)")
    length = models.PositiveIntegerField(verbose_name="Length (in.)")
    turn = models.PositiveIntegerField(verbose_name="Turn circle (ft.)")
    displacement = models.PositiveIntegerField(verbose_name="Displacement (cu. in.)")
    gear_ratio = models.FloatField(verbose_name="Gear ratio")
    foreign = models.BooleanField(verbose_name="Car origin (foreign)")
    
    creation_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Make : {self.make.name}, Model : {self.name}, Weight: {self.weight}."