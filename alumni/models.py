from django.db import models
from django.contrib.auth.models import User 
from django.shortcuts import reverse
# Create your models here.

STATUS_CHOICES = (("student","Student"),("alumni","Alumni"))
YEAR_CHOICES = (("1st year","1st year"),("2nrd year","2nd year"),("3rd year","3rd year"),("4th year","4th year"),("Working","Working"))

class Projects(models.Model):
    title = models.CharField(max_length=500)
    #author_name = models.CharField(max_length=500,default='Enter your username')
    student1 = models.CharField(max_length=500,null=True)
    student2 = models.CharField(max_length=500,null=True)
    student3 = models.CharField(max_length=500,null=True)
    description = models.TextField()
    tech_stack = models.TextField() 
    working_ss = models.ImageField(upload_to='project') 
    mentor = models.ManyToManyField('Profile',blank=True,related_name='mentor')  

    def get_absolute_url(self):
        return reverse('prodetails',kwargs={'id':self.id})



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=500,null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    email_id = models.EmailField(null=True)
    mobile_no = models.IntegerField(null=True) 
    current_year = models.CharField(null=True,choices=YEAR_CHOICES,max_length=500)
    status = models.CharField(default='choice',max_length=300,choices=STATUS_CHOICES) 
    short_note_about_yourself = models.TextField(null=True)
    company_or_organisation = models.CharField(max_length=500,null=True)

    def __str__(self):
        return f'{self.user.username}'

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs) 



