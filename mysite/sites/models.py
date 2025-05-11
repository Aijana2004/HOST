from django.db import models
from  django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    user_role = models.CharField(max_length=40,choices=[('host','host'),('guest','guest'),('admin','admin'),])
    phone_number = PhoneNumberField(region='KG',null=True,blank=True)
    avatar = models.ImageField(upload_to='property_images/')


class Property(models.Model):
    title =models.CharField(max_length=100)
    description = models.TextField()
    price =models.PositiveSmallIntegerField(default=0)
    per_night =models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    property_type = models.CharField(max_length=40,choices=[('apartment','apartment'),('house','house'),('house','house'),])
    rules = models.CharField(max_length=40,choices=[('no_smoking','no_smoking'),('pets_allowed','pets_allowed')])
    max_guests = models.CharField(max_length=100)
    bedroom =models.CharField(max_length=100)
    bathroom=models.CharField(max_length=100)
    owner = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='owner')
    is_active =models.CharField(max_length=100)


class Photos(models.Model):
    home_photo = models.ForeignKey(Property,related_name='property_photos',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')


class Booking(models.Model):
    property = models.ForeignKey(Property,on_delete=models.CASCADE,related_name='property')
    guest =models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='guest')
    check_in = models.DateField()
    check_out = models.DateField()
    status = models.CharField(max_length=40, choices=[('pending', 'pending'),
                                                      ('approved', 'approved'),
                                                      ('rejected', 'rejected'),
                                                      ('cancelled', 'cancelled'), ])

    created_at = models.DateField(auto_now_add=True)


class Review(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='propertyes')
    guest = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='guests')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)






