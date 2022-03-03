from django.db import models

class ImageDB(models.Model):
    pathh = models.CharField(max_length=100)
    # # pathh = models.CharField(max_length=100)
    des = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.pathh} - {self.des}'

