
from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=100,null=True)
    address = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=50,null=True)
    image = models.ImageField(default='default.png', upload_to='profile_images',null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
  
   

    def __str__(self):
        return f'{self.staff.username}-Profile'

class Position(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Candidate(models.Model):
    name = models.CharField(max_length=50)
    total_vote = models.IntegerField(default=0, editable=False)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Candidate Pic", upload_to='images/')
    text = models.TextField()

    def __str__(self):
        return "{} - {}".format(self.name, self.position.title)


class ControlVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.user, self.status)
