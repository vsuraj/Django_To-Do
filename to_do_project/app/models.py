from django.db import models

# Create your models here.
class add_task(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField(null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)