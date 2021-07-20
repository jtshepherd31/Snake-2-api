from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Highscore(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  email = models.CharField(max_length=100)
  score = models.CharField(max_length=100)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The highscore of '{self.email}' is {self.score}."

  def as_dict(self):
    """Returns dictionary version of Highscore models"""
    return {
        'id': self.id,
        'email': self.email,
        'score': self.score
    }
