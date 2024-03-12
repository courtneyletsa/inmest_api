from django.db import models
from django.contrib.auth.models import *
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

# Create your models here.
class IMUser(AbstractUser):
    first_name = models.CharField(max_length=155, blank=True)
    last_name = models.CharField(max_length=155, blank=True)
    middle_name = models.CharField(max_length=155, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    USER_TYPES = [
        ('EIT', 'EiT'),
        ('TEACHING_FELLOW', 'Teaching Fellow'),
        ('ADMIN_STAFF', 'Administrative Staff'),
        ('ADMIN', 'Administrator'),
    ]

    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='EIT')
    date_created = models.DateTimeField(auto_now_add=True)
    unique_code=models.CharField(max_length=20, blank=True)
    groups = models.ManyToManyField(Group, related_name='imuser_set')
    user_permissions = models.ManyToManyField(Permission, related_name='imuser_set')
    is_blocked = models.BooleanField(default=False)
    temporal_login_fail = models.IntegerField(default=0)
    permanant_login_fail = models.IntegerField(default=0)
    
    def _str_(self):
        return f"{self.first_name} {self.last_name}"


@receiver(post_save, sender=IMUser)    
def generate_auth_token(sender, instance=None, created=False,**kwargs):
    if created:
        token = Token.objects.create(user=instance)
        token.save()
    
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


class CohorMember(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete = models.CASCADE)
    members = models.ForeignKey(IMUser, on_delete = models.CASCADE, related_name='cohort_members') 
    is_active = models.BooleanField(default = False)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)  
    author = models.ForeignKey(IMUser, on_delete = models.CASCADE, related_name='authored_members')
    
    def __str__(self):
        return f"(self.member.first_name) in (self.cohort.name)"
    
    
    
    