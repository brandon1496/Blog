from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class User(models.Model):
    author = models.CharField(max_length=20)

    def __str__(self):
        return self.author

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    #date = models.DateField(defualt= auto_now_add=True)
    #pub_date = models.DateTimeField('date published')
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.title
