from django.db import models

# Create your models here.
class UserType(models.Model):
    name = models.CharField(max_length = 225, unique = True)
    
    def __str__(self):
        return self.name

class IMUser(models.Model):
    first_name = models.CharField(max_length = 500, null = False)
    last_name = models.CharField(max_length = 500, null = False)
    is_active = models.BooleanField(default=False)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.first_name
    
class Cohort(models.Model):
    name = models.CharField(max_length = 500, null = False)
    description = models.TextField(max_length = 5000, blank = True)
    year = models.IntegerField()
    start_date = models.DateField(blank = True)
    end_date = models.DateField(blank = True)
    is_active = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, blank =True, null = True)
    date_modified = models.DateTimeField(auto_now=True, blank =True, null = True)
    author = models.ForeignKey(IMUser, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name
    
    