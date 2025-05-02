from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length = 64)
    password = models.CharField(max_length = 64)

    def __str__(self):
        return f"{self.name} {self.password}"

class exercise(models.Model):
    user_name = models.CharField(max_length = 64)
    exercise_name = models.CharField(max_length = 64)
    sets = models.IntegerField()
    reps = models.IntegerField()

    def __str__(self):
        return f"User {self.user_name} Exercise {self.exercise_name}"