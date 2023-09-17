from django.db import models

# Create your models here.
class PostAPIModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    createAT = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title