from django.db import models
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=120)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_url_update(self):
        return reverse('tasks:update', kwargs={'my_id':self.id})

    def get_url_delete(self):
        return reverse('tasks:delete', kwargs={'my_id':self.id})