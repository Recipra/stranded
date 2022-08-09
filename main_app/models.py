from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

TYPES = (
  ('T', 'Tool'),
  ('S', 'Shelter'),
  ('O', 'Outfit')
)

DURABILITY = (
  ('W', 'Worn'),
  ('U', 'Used'),
  ('N', 'Unused')
)

RATINGS = (
  ('1', '1'),
  ('2', '2'),
  ('3', '3'),
  ('4', '4'),
  ('5', '5')
)

# Create your models here.

class Equipment(models.Model):
  name = models.CharField(max_length=50)
  type = models.CharField(max_length=1, choices=TYPES, default=TYPES[0][0])
  description = models.TextField(max_length=200)
  durability = models.CharField(max_length=1, choices=DURABILITY, default=DURABILITY[0][0])
  rating = models.CharField(max_length=1, choices=RATINGS, default=RATINGS[0][0])

  def __str__(self):
    return self.name