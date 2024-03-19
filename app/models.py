from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField()
    first_name = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name
    
    
class Projects(models.Model):
    title = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return self.title
    
class Task(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateField(auto_now=True)
    status = models.CharField(max_length = 50)
    project = models.ForeignKey(Projects, on_delete = models.CASCADE)
    def __str__(self):
        return self.title