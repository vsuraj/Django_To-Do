from django.db import models

# Create your models here.
class task(models.Model):
    task_title = models.CharField(max_length=100)
    task_discription = models.TextField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    task_status = models.BooleanField(default=False)
