from django.db import models

# Create your models here.
class todo(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class item(models.Model):
    todovar = models.ForeignKey(todo, on_delete=models.CASCADE)