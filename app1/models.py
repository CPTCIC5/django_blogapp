from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Posts(models.Model):
    title=models.TextField()
    content=models.CharField(max_length=8000,default='content', null=False)
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.title}"  

    class Meta():
        verbose_name_plural='Post"s'