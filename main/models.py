from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=30)
    event_image = models.ImageField(upload_to="images/",default="https://upload.wikimedia.org/wikipedia/en/b/b0/IEEE_Communications_Society_Logo.png")
    speaker = models.CharField(max_length=30)
    event_description = models.CharField(max_length=100,default="about")
    event_data = models.DateTimeField()

    def __str__(self):
        return self.event_name


class event_reg(models.Model):
    event = models.ForeignKey(Event,on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    regno = models.CharField(max_length=12)
    email = models.EmailField()
    phone = models.IntegerField()

class blog(models.Model):
    Title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    author_pic = models.ImageField(upload_to="images/")
    blog_link = models.URLField()


class posts(models.Model):
    post_name = models.CharField(max_length=50)
    post_image = models.ImageField(upload_to="images/")


