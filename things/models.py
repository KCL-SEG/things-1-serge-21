from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Thing(models.Model):
    # name: a short string that identifies a thing.
    # name must be unique, must not be blank, and must consist of 30 characters or less.
    name = models.CharField(blank = False, unique = True, max_length = 30)
    
    # description: a slightly longer string that describes a thing.
    # description need not be unique, may be blank, and must consist of 120 characters of less.
    description = models.CharField(blank = True, unique = False, max_length = 120)

    # quantity: an integer that identifies the number of items of a thing we possess.
    # quantity need not be unique, and must be an integer value between 0 and 100 (inclusive). quantity may be 0 and it may be 100, but not less than 0 and not more than 100.
    quantity = models.IntegerField(unique = False, validators=[MinValueValidator(0), MaxValueValidator(100)])