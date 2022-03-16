from django.db import models

class MusicLibrary(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    length = models.CharField(max_length=8)
    


