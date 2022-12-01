from django.contrib.auth.models import User
from django.db import models


class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    image = models.ImageField(default='profile.jpg',upload_to='profile_pictures')
    address = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return '%s' % self.user.username

User.userprofile = property(lambda u:Userprofile.objects.get_or_create(user=u)[0])


 
class Contact(models.Model):
    fullname = models.CharField(max_length=20, null=True)
    phonenumber = models.CharField(max_length=11, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email