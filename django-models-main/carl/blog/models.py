from webbrowser import get
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text= models.TextField
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_date = models.DateTimeField('Created date')
    published_date = models.DateTimeField('Published date')