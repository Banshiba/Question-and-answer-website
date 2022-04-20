from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class questions(models.Model):
    title=models.CharField(max_length=1000)
    Content=models.TextField(null=True ,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("qs-details", kwargs={"pk": self.pk})
    
    def getanswers(self):
        return self.ans.filter(parent=None)

class Comment(models.Model):
    question=models.ForeignKey(questions, related_name ="comment", on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now) 
    

     

    def __str__(self):
        return (self.question.id)

    def get_success_url(self):
        return reverse('questions_detail', kwargs={'pk':self.pk})
    
    def total_likes(self):
        return (self.likes.count())
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
     
    