from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField # On importe le champ spécial Cloudinary

class Hotel(models.Model):
    # Ajout du lien entre l'hôtel et l'utilisateur (Admin)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hotels', null=True, blank=True)
    
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    
    # REMPLACE models.ImageField par CloudinaryField
    image = CloudinaryField('image', null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name