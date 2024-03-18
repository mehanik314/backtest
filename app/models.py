from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField
    first_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user_id
    
    
class Projects(models.Model):
    project_title = models.CharField(max_length=50)
    project_desc = models.CharField(max_length=100)

    def __str__(self):
        return self